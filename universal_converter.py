#!/usr/bin/env python3
"""
Universal File Converter
Supports: Images, Videos, Documents, Audio
"""

import os
import sys
import subprocess
import mimetypes
from pathlib import Path
import argparse

class FileConverter:
    def __init__(self):
        self.supported_conversions = {
            'image': {
                'input': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
                'output': ['.jpg', '.png', '.pdf', '.webp', '.bmp', '.ico'],
                'tool': 'pillow'
            },
            'video': {
                'input': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm'],
                'output': ['.mp4', '.avi', '.mov', '.webm', '.gif'],
                'tool': 'ffmpeg'
            },
            'audio': {
                'input': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
                'output': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
                'tool': 'ffmpeg'
            },
            'document': {
                'input': ['.docx', '.pdf', '.txt', '.rtf', '.odt', '.html', '.md'],
                'output': ['.pdf', '.html', '.txt', '.md'],
                'tool': 'pypandoc'
            }
        }
    
    def detect_file_type(self, filepath):
        """Detect the category of the file"""
        ext = Path(filepath).suffix.lower()
        for category, specs in self.supported_conversions.items():
            if ext in specs['input']:
                return category
        return None
    
    def convert_with_pillow(self, input_path, output_path):
        """Convert images using Pillow"""
        try:
            from PIL import Image
            img = Image.open(input_path)
            
            # Convert RGBA to RGB if saving as JPEG
            if output_path.lower().endswith('.jpg') and img.mode == 'RGBA':
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
                img = rgb_img
            
            # Handle ICO conversion
            if output_path.lower().endswith('.ico'):
                img.thumbnail((256, 256), Image.Resampling.LANCZOS)
            
            img.save(output_path)
            return True, output_path
        except Exception as e:
            return False, str(e)
    
    def convert_with_ffmpeg(self, input_path, output_path):
        """Convert video/audio using FFmpeg"""
        ext = Path(output_path).suffix.lower()
        
        # Check if FFmpeg is available
        if not shutil.which('ffmpeg'):
            return False, "FFmpeg not installed. Download from https://ffmpeg.org"
        
        if ext == '.gif':
            # Video to GIF
            cmd = [
                'ffmpeg', '-i', input_path,
                '-vf', 'fps=10,scale=320:-1:flags=lanczos',
                '-c:v', 'gif', '-f', 'gif',
                output_path, '-y'
            ]
        else:
            # General conversion
            cmd = ['ffmpeg', '-i', input_path, output_path, '-y']
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                return True, output_path
            else:
                return False, result.stderr
        except Exception as e:
            return False, str(e)
    
    def convert(self, input_path, output_format):
        """Main conversion method"""
        input_path = Path(input_path)
        if not input_path.exists():
            return False, "Input file not found"
        
        file_type = self.detect_file_type(input_path)
        if not file_type:
            return False, "Unsupported input format"
        
        # Check if output format is supported
        if output_format not in self.supported_conversions[file_type]['output']:
            return False, f"Cannot convert {file_type} to {output_format}"
        
        # Generate output path
        output_path = input_path.with_suffix(output_format)
        
        # Perform conversion
        if file_type == 'image':
            return self.convert_with_pillow(str(input_path), str(output_path))
        elif file_type in ['video', 'audio']:
            return self.convert_with_ffmpeg(str(input_path), str(output_path))
        else:
            return False, "Document conversion requires additional tools"

def main():
    parser = argparse.ArgumentParser(description='Universal File Converter')
    parser.add_argument('input', nargs='?', help='Input file path')
    parser.add_argument('-o', '--output', help='Output format (e.g., .pdf, .mp3)')
    parser.add_argument('--list', action='store_true', help='List supported formats')
    
    args = parser.parse_args()
    
    converter = FileConverter()
    
    if args.list:
        print("Supported Conversions:")
        for category, specs in converter.supported_conversions.items():
            print(f"\n{category.upper()}:")
            print(f"  Input:  {', '.join(specs['input'])}")
            print(f"  Output: {', '.join(specs['output'])}")
        return
    
    if not args.input:
        parser.print_help()
        return
    
    if not args.output:
        print("Error: Please specify output format with -o")
        return
    
    success, result = converter.convert(args.input, args.output)
    if success:
        print(f"✅ Conversion successful: {result}")
    else:
        print(f"❌ Conversion failed: {result}")
        sys.exit(1)

if __name__ == '__main__':
    # Install required packages if missing
    try:
        from PIL import Image
    except ImportError:
        print("Installing Pillow for image conversion...")
        subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"])
    
    main()