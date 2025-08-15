from PDFGenerator import PDFGenerator
from topics import TopicReader

# Define constants for configuration at the top of the file
INPUT_FILE = "topics.csv"
OUTPUT_FILE = "output.pdf"

def main():
    """
    Main function to orchestrate the PDF generation.
    """
    reader = TopicReader(INPUT_FILE)
    topics_list = reader.get_topics()
    
    if not topics_list:
        print("No topics found. Exiting the program.")
        return

    generator = PDFGenerator()

    print("Starting PDF generation...")
    for topic in topics_list:
        print(f"- Processing topic: {topic['Topic']}")
        # Add the main topic page
        generator.add_topic_pg(topic["Topic"])
        
        # Add the extra pages
        for _ in range(topic["Pages"] - 1):
            generator.add_extra_pg(topic["Topic"])

    generator.output(OUTPUT_FILE)
    print(f"PDF successfully created at '{OUTPUT_FILE}'!")


# Main
if __name__ == "__main__":
    main()