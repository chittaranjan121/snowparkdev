import sys
import os

directory_path = sys.argv[1]
os.chdir(directory_path)

print("🔧 Building Snowpark project...")
os.system("snow snowpark build")

print("🚀 Deploying Snowpark project...")

cmd = """
snow snowpark deploy --replace --temporary-connection \
--account "{account}" \
--user "{user}" \
--password "{password}" \
--role "{role}" \
--warehouse "{warehouse}" \
--database "{database}" \
--schema "{schema}"
""".format(
    account=os.environ["SNOWFLAKE_ACCOUNT"],
    user=os.environ["SNOWFLAKE_USER"],
    password=os.environ["SNOWFLAKE_PASSWORD"],
    role=os.environ["SNOWFLAKE_ROLE"],
    warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
    database=os.environ["SNOWFLAKE_DATABASE"],
    schema=os.environ["SNOWFLAKE_SCHEMA"],
)

exit_code = os.system(cmd)
if exit_code != 0:
    raise RuntimeError("❌ Snowpark deployment failed")

print("✅ Snowpark deployment completed successfully")
