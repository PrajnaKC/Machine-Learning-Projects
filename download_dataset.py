"""
Dataset Setup Helper for Movie Recommendation System

This script helps you check and set up the required TMDB movie dataset.
"""

import os
from pathlib import Path

class DatasetDownloader:
    def __init__(self):
        self.project_dir = Path(__file__).parent
        self.required_files = ['tmdb_5000_movies.csv', 'tmdb_5000_credits.csv']
        
    def check_files_exist(self):
        """Check if the required dataset files already exist"""
        existing_files = []
        missing_files = []
        
        for file in self.required_files:
            file_path = self.project_dir / file
            if file_path.exists():
                existing_files.append(file)
                print(f"✓ Found: {file}")
            else:
                missing_files.append(file)
                print(f"✗ Missing: {file}")
        
        return existing_files, missing_files
    
    def verify_file_format(self, file_path):
        """Verify if the CSV file has the expected format"""
        try:
            import pandas as pd
            df = pd.read_csv(file_path, nrows=5)  # Read only first 5 rows for verification
            
            if 'tmdb_5000_movies.csv' in str(file_path):
                expected_columns = ['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 
                                  'original_title', 'overview', 'popularity', 'production_companies']
                if any(col in df.columns for col in expected_columns):
                    print(f"✓ {file_path.name} appears to have correct format")
                    return True
                    
            elif 'tmdb_5000_credits.csv' in str(file_path):
                expected_columns = ['movie_id', 'title', 'cast', 'crew']
                if any(col in df.columns for col in expected_columns):
                    print(f"✓ {file_path.name} appears to have correct format")
                    return True
            
            print(f"⚠ {file_path.name} may not have the expected format")
            return False
            
        except Exception as e:
            print(f"⚠ Could not verify {file_path.name}: {e}")
            return False
    
    def download_with_kaggle_api(self):
        """Download dataset using Kaggle API"""
        try:
            import kaggle
            print("Attempting to download using Kaggle API...")
            
            # Download the dataset
            kaggle.api.dataset_download_files(
                'tmdb/tmdb-movie-metadata',
                path=str(self.project_dir),
                unzip=True
            )
            
            print("✓ Dataset downloaded successfully using Kaggle API!")
            return True
            
        except ImportError:
            print("⚠ Kaggle API not installed.")
            return False
        except Exception as e:
            print(f"⚠ Kaggle API download failed: {e}")
            return False
    
    def show_upload_instructions(self):
        """Show detailed instructions for manually placing dataset files"""
        print("\n" + "="*70)
        print("📁 HOW TO UPLOAD/PLACE DATASET FILES")
        print("="*70)
        print(f"📂 Your project folder location:")
        print(f"   {self.project_dir}")
        print()
        print("🔽 STEP-BY-STEP INSTRUCTIONS:")
        print()
        print("Option 1: Download from Kaggle")
        print("-" * 30)
        print("1. Open your web browser")
        print("2. Go to: https://www.kaggle.com/tmdb/tmdb-movie-metadata")
        print("3. Sign in to Kaggle (create free account if needed)")
        print("4. Click the blue 'Download' button")
        print("5. A file called 'tmdb-movie-metadata.zip' will download")
        print("6. Right-click the ZIP file → 'Extract All'")
        print("7. Open the extracted folder")
        print("8. Copy these 2 files:")
        print("   • tmdb_5000_movies.csv")
        print("   • tmdb_5000_credits.csv")
        print(f"9. Paste them into: {self.project_dir}")
        print()
        print("Option 2: Using File Explorer")
        print("-" * 30)
        print("1. Open File Explorer (Windows key + E)")
        print(f"2. Navigate to: {self.project_dir}")
        print("3. If you already have the CSV files:")
        print("   • Drag and drop them into this folder")
        print("   • Or copy-paste them here")
        print()
        print("Option 3: From USB/External Drive")
        print("-" * 30)
        print("1. Connect your USB drive/external storage")
        print("2. Open File Explorer")
        print("3. Navigate to your files on the external drive")
        print("4. Copy the CSV files")
        print(f"5. Navigate to: {self.project_dir}")
        print("6. Paste the files")
        print()
        print("📋 IMPORTANT NOTES:")
        print("• Files must be named EXACTLY:")
        print("  - tmdb_5000_movies.csv")
        print("  - tmdb_5000_credits.csv")
        print("• Files must be in CSV format (not Excel .xlsx)")
        print("• Place files directly in the project folder (not in subfolders)")
        print()
        print("🔍 TO VERIFY: Run this script again after placing files")
        print("="*70)
    
    def run(self):
        """Main function to check and download dataset"""
        print("Movie Recommendation System - Dataset Setup")
        print("="*50)
        
        # Check current status
        existing, missing = self.check_files_exist()
        
        if not missing:
            print(f"\n✓ All required files are present!")
            
            # Verify file formats
            print("\nVerifying file formats...")
            for file in existing:
                self.verify_file_format(self.project_dir / file)
            
            print(f"\n🎉 Dataset setup complete! You can now run:")
            print(f"   python movie_recommendation_system.py")
            return
        
        print(f"\n📥 Missing {len(missing)} file(s).")
        
        # Show manual instructions
        self.show_upload_instructions()
        
        # Try Kaggle API as alternative
        print("\n🤖 ALTERNATIVE: Automatic Download")
        print("-" * 40)
        response = input("Would you like to try automatic download via Kaggle API? (y/n): ")
        if response.lower().startswith('y'):
            if self.download_with_kaggle_api():
                print("\nRechecking files...")
                self.check_files_exist()
                return
        
        # Additional help
        print("\nTROUBLESHOTING:")
        print("- Make sure you have a Kaggle account")
        print("- Verify your internet connection")
        print("- Check that files are named exactly as shown above")
        print("- Files should be in CSV format, not Excel or other formats")

if __name__ == "__main__":
    downloader = DatasetDownloader()
    downloader.run()