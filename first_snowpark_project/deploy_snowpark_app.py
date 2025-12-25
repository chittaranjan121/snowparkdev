import sys
import os

directory_path = sys.argv[1]
os.chdir(directory_path)

print("🔧 Building Snowpark project...")
if os.system("snow snowpark build") != 0:
    raise RuntimeError("❌ Build failed")

print("📂 Verifying artifacts...")
os.system("ls -R artifacts")

print("🚀 Deploying Snowpark project...")
if os.system("snow snowpark deploy --replace") != 0:
    raise RuntimeError("❌ Deploy failed")

print("✅ Snowpark deployment completed successfully")
