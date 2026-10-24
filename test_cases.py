from solutions import solve_max_profit

def run_tests():
    test_cases = [
        {"input": 7, "expected_earnings": 3000},  #[cite: 1]
        {"input": 8, "expected_earnings": 4500},  #[cite: 1]
        {"input": 13, "expected_earnings": 16500} #[cite: 1]
    ]
    
    for i, tc in enumerate(test_cases, 1):
        n = tc["input"]
        earnings, mix = solve_max_profit(n)
        print(f"Test Case {i} (Time Unit: {n}): Earnings = ${earnings} | Mix = {mix}")
        assert earnings == tc["expected_earnings"], f"Test {i} failed!"
        
    print("\nAll test cases passed successfully!")

if __name__ == "__main__":
    run_tests()