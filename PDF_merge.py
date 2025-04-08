from PyPDF2 import PdfMerger

def merge_pdfs(file_paths, output_path):
    """
    Merge multiple PDF files into a single PDF.

    :param file_paths: List of file paths to the PDF files to be merged.
    :param output_path: Path to save the merged PDF.
    """
    merger = PdfMerger()
    try:
        for file_path in file_paths:
            merger.append(file_path)
        merger.write(output_path)
        print(f"Merged PDF saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        merger.close()

# Example usage
if __name__ == "__main__":
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]  # Replace with your file paths
    output_file = "merged_output.pdf"
    merge_pdfs(pdf_files, output_file)