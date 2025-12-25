import sys
import os

project_dir = sys.argv[1]
os.chdir(project_dir)

print("🔧 Building Snowpark project...")
build_code = os.system(
    "snow snowpark build --connection default"
)
if build_code != 0:
    raise RuntimeError("❌ Build failed")

print("🚀 Deploying Snowpark project...")
deploy_code = os.system(
    "snow snowpark deploy --replace --temporary-connection"
)

if deploy_code != 0:
    raise RuntimeError("❌ Snowpark deployment failed")

print("✅ Snowpark deployment completed successfully")
