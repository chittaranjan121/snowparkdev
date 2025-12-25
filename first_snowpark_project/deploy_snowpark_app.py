import sys
import os

directory_path = sys.argv[1]
os.chdir(directory_path)

print("🔧 Building Snowpark project...")
if os.system("snow snowpark build") != 0:
    raise RuntimeError("❌ Build failed")

print("🚀 Deploying Snowpark project...")
deploy_cmd = """
snow snowpark deploy --replace --temporary-connection
"""

if os.system(deploy_cmd) != 0:
    raise RuntimeError("❌ Deploy failed")

print("✅ Snowpark deployment completed successfully")
