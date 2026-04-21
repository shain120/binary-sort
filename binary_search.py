def binary_search(arr, target, left, right):
    """使用二元搜尋找到 target 應插入的位置"""
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def binary_insertion_sort(arr):
    """
    二元插入排序：
    - 插入排序的改良版，用二元搜尋取代線性搜尋
    - 比較次數：O(n log n)
    - 移動次數：O(n²)（最壞情況）
    - 空間複雜度：O(1)（原地排序）
    """
    for i in range(1, len(arr)):
        key = arr[i]

        # 用二元搜尋找到插入位置
        pos = binary_search(arr, key, 0, i)

        # 將 pos ~ i-1 的元素往右移一格
        arr[pos + 1 : i + 1] = arr[pos:i]
        arr[pos] = key

    return arr


# ── 測試 ──────────────────────────────────────────────────────────────────────

def run_tests():
    test_cases = [
        {
            "desc": "一般亂序",
            "data": [64, 34, 25, 12, 22, 11, 90],
        },
        {
            "desc": "已排序",
            "data": [1, 2, 3, 4, 5],
        },
        {
            "desc": "逆序",
            "data": [9, 7, 5, 3, 1],
        },
        {
            "desc": "含重複元素",
            "data": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        },
        {
            "desc": "單一元素",
            "data": [42],
        },
        {
            "desc": "空陣列",
            "data": [],
        },
        {
            "desc": "負數與正數混合",
            "data": [-5, 3, -1, 0, 7, -8, 2],
        },
    ]

    print("=" * 50)
    print("  Binary Insertion Sort 測試")
    print("=" * 50)

    all_passed = True
    for tc in test_cases:
        original = tc["data"][:]
        result = binary_insertion_sort(tc["data"][:])
        expected = sorted(original)
        passed = result == expected

        status = "✅ PASS" if passed else "❌ FAIL"
        if not passed:
            all_passed = False

        print(f"\n{status}  {tc['desc']}")
        print(f"  輸入：{original}")
        print(f"  輸出：{result}")
        if not passed:
            print(f"  期望：{expected}")

    print("\n" + "=" * 50)
    print("  所有測試通過！" if all_passed else "  有測試失敗，請檢查！")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

    # 互動示範
    print("\n── 互動示範 ──")
    user_input = input("請輸入數字（以空格分隔）：")
    numbers = list(map(int, user_input.split()))
    sorted_numbers = binary_insertion_sort(numbers[:])
    print(f"排序前：{numbers}")
    print(f"排序後：{sorted_numbers}")
