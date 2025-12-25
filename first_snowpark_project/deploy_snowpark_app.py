import sys
import os

project_dir = sys.argv[1]
os.chdir(project_dir)

print("🔧 Building Snowpark project...")
if os.system("snow snowpark build --connection default") != 0:
    raise RuntimeError("❌ Build failed")

print("🚀 Deploying Snowpark project...")
if os.system("snow snowpark deploy --replace --connection default") != 0:
    raise RuntimeError("❌ Deploy failed")

print("✅ Snowpark deployment completed successfully")
