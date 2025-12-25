import sys
import os

# Path to snowpark project
project_dir = sys.argv[1]
os.chdir(project_dir)

print("🔧 Building Snowpark project...")
build_status = os.system("snow snowpark build --connection default")
if build_status != 0:
    raise RuntimeError("❌ Build failed")

print("🚀 Deploying Snowpark project...")
deploy_status = os.system("snow snowpark deploy --replace --connection default")
if deploy_status != 0:
    raise RuntimeError("❌ Deploy failed")

print("✅ Snowpark deployment completed successfully")
