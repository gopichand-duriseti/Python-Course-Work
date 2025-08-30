import os
import re


# Positive Food Review Words
POSITIVE_WORDS = {
    "flavorful", "crispy", "fresh", "creamy", "rich",
    "buttery", "soft", "satisfying", "authentic", "colorful",
    "warm", "refreshing", "balanced", "heavenly", "delightful",
    "tasty", "crunchy", "aromatic", "juicy", "perfect",
    "smooth", "appetizing", "wholesome", "generous", "delicious"
}

# Negative Food Review Words
NEGATIVE_WORDS = {
    "soggy", "bland", "watery", "artificial", "disappointing",
    "overpriced", "undercooked", "stale", "greasy", "burnt",
    "salty", "cold", "boring", "tasteless", "chewy",
    "oily", "bitter", "unseasoned", "raw", "spoiled",
    "overcooked", "small", "flavorless", "messy", "dull"
}


# Directory where Food reviews are stored
foodreviews_dir = "Assignments/Foods_related_notes/Foodreviews"

print("Looking for reviews in:", os.path.abspath(foodreviews_dir))

# Ensure the directory exists
os.makedirs(foodreviews_dir, exist_ok=True)

#Clean filename: strip spaces and ensure .txt extension.
def text_filename(filename):
    filename = filename.strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

#Analyze review content and determine if it has a positive or negative vibe.
def analyze_sentiment(content):
    positive_count = len(re.findall(r'\b(?:' + '|'.join(POSITIVE_WORDS) + r')\b', content, re.IGNORECASE))
    negative_count = len(re.findall(r'\b(?:' + '|'.join(NEGATIVE_WORDS) + r')\b', content, re.IGNORECASE))

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

#Read and analyze a specific review or all reviews.
def read_and_analyze_note():
    choice = input("Do you want to analyze:\n1. A specific recipe review\n2. All recipes reviews\nEnter your choice: ").strip()

    if choice == "1":
        filename = input("Enter the file name: ")
        filename = text_filename(filename)
        file_path = os.path.join(foodreviews_dir, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                sentiment = analyze_sentiment(content)
                print(f"\nAnalyzing file: {filename}\nDetected Sentiment: {sentiment}\n")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found in {foodreviews_dir}.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":
        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
        files = os.listdir(foodreviews_dir)

        if not files:
            print("No reviews found.")
            return

        for filename in files:
            file_path = os.path.join(foodreviews_dir, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                sentiment = analyze_sentiment(content)
                sentiment_counts[sentiment] += 1

        print("\nOverall Sentiment Analysis:")
        for sentiment, count in sentiment_counts.items():
            print(f"{sentiment}: {count} reviews")

#Create a new review note.
def create_note():
    filename = input("Enter the name of the new review: ")
    filename = text_filename(filename)
    file_path = os.path.join(foodreviews_dir, filename)

    content = input("Enter your review content:\n")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print()
    print(f"Review '{filename}' saved successfully.")

#Modify an existing review note.
def modify_note():
    files = os.listdir(foodreviews_dir)
    if not files:
        print("No reviews available to modify.")
        return

    print("Existing reviews:",files)
    filename = input("Enter the file name to modify: ")
    filename = text_filename(filename)
    file_path = os.path.join(foodreviews_dir, filename)

    if not os.path.exists(file_path):
        print(f"Error: File '{filename}' not found in {foodreviews_dir}.")
        return

    new_content = input("Enter new content:\n")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"Review '{filename}' updated successfully.")

#Main function to run the Movie Review Notes Management System.
def main():
    while True:
        print("\n🎬 Intelligent Food Review Notes Management System")
        print("1. Read & Analyze Reviews")
        print("2. Create a New Review")
        print("3. Modify an Existing Review")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            read_and_analyze_note()
        elif choice == "2":
            create_note()
        elif choice == "3":
            modify_note()
        elif choice == "4":
            print("Exiting....")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()