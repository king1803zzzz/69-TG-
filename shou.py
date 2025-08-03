import os

def list_all_environment_variables():
    """
    列出当前执行环境中的所有环境变量及其值。
    """
    print("--- Listing All Environment Variables ---")

    # 获取所有环境变量的键并按字母顺序排序，以便于阅读
    sorted_keys = sorted(os.environ.keys())

    for key in sorted_keys:
        value = os.environ[key]
        print(f"- {key}: {value}")

    print("\n---------------------------------------")
    print("Note: If a variable's value looks like '***', it's likely a GitHub Secret automatically masked.")

if __name__ == "__main__":
    list_all_environment_variables()
