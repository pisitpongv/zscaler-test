# dlp_test_data.py
# BENIGN DATA — for DLP testing only



def generate_text():
    output = []

    for category, values in test_data.items():
        output.append(f"\n===== {category.upper()} =====")

        for key, value in values.items():
            output.append(f"{key}: {value}")

    return "\n".join(output)


if __name__ == "__main__":
    print(generate_text())