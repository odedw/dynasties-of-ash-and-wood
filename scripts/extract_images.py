#!/usr/bin/env python3
"""
Extract inline base64 images from a markdown file and save them as external files.
Updates the markdown to reference the external image files.
"""

import re
import base64
import sys
from pathlib import Path


def extract_images(markdown_path: Path, output_dir: Path):
    """
    Extract base64 images from markdown and save to output directory.
    
    Args:
        markdown_path: Path to the markdown file
        output_dir: Directory to save extracted images
    """
    # Read the markdown file
    content = markdown_path.read_text(encoding='utf-8')
    
    # Pattern to match image definitions like [image1]: <data:image/png;base64,...>
    image_def_pattern = re.compile(
        r'^\[([^\]]+)\]:\s*<data:image/([^;]+);base64,([^>]+)>',
        re.MULTILINE
    )
    
    # Find all image definitions
    matches = list(image_def_pattern.finditer(content))
    
    if not matches:
        print("No inline images found.")
        return
    
    print(f"Found {len(matches)} inline images")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Track replacements to make
    replacements = {}
    
    for match in matches:
        image_name = match.group(1)
        image_format = match.group(2)
        base64_data = match.group(3)
        
        # Determine file extension
        ext = image_format.lower()
        if ext == 'jpeg':
            ext = 'jpg'
        
        # Create filename
        filename = f"{image_name}.{ext}"
        filepath = output_dir / filename
        
        # Decode and save the image
        try:
            image_data = base64.b64decode(base64_data)
            filepath.write_bytes(image_data)
            print(f"  Extracted: {filename} ({len(image_data):,} bytes)")
        except Exception as e:
            print(f"  Error extracting {image_name}: {e}")
            continue
        
        # Calculate relative path from markdown file to image
        # For mkdocs, we want paths relative to the markdown file's location
        rel_path = Path("images") / filename
        
        # Store the replacement: old definition -> new definition
        replacements[match.group(0)] = f"[{image_name}]: {rel_path}"
    
    # Remove old image definitions and add new ones
    new_content = content
    for old_def, new_def in replacements.items():
        new_content = new_content.replace(old_def, new_def)
    
    # Write updated markdown
    markdown_path.write_text(new_content, encoding='utf-8')
    print(f"\nUpdated {markdown_path}")
    print(f"Images saved to {output_dir}")


def main():
    # Default paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    markdown_file = project_root / "docs" / "resources" / "Player Guide.md"
    output_dir = project_root / "docs" / "resources" / "images"
    
    # Allow overriding via command line arguments
    if len(sys.argv) >= 2:
        markdown_file = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    
    if not markdown_file.exists():
        print(f"Error: Markdown file not found: {markdown_file}")
        sys.exit(1)
    
    print(f"Processing: {markdown_file}")
    print(f"Output directory: {output_dir}")
    print()
    
    extract_images(markdown_file, output_dir)


if __name__ == "__main__":
    main()
