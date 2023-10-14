import os
import math
import tempfile
from pdfminer.high_level import extract_text

def split_pdf(file_path, chunk_size):
    """
    Splits a PDF file into smaller chunks and returns a list of file paths for each chunk.
    :param file_path: The path to the PDF file to split.
    :param chunk_size: The size of each chunk (in number of pages).
    :return: A list of file paths for each chunk.
    """
    # Get the total number of pages in the PDF file
    total_pages = len(list(extract_text(file_path)))

    # If the PDF file is already small enough, return the file path as a list
    if total_pages <= chunk_size:
        return [file_path]

    # Calculate the number of chunks required to split the PDF file
    num_chunks = math.ceil(total_pages / chunk_size)

    # Create a temporary directory to store the split PDF files
    temp_dir = tempfile.mkdtemp()

    # Split the PDF file into smaller chunks and save each chunk as a separate file
    file_paths = []
    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, total_pages)
        pages = list(range(start + 1, end + 1))
        temp_path = os.path.join(temp_dir, f"chunk_{i+1}.pdf")
        os.system(f"pdfseparate -f {start+1} -l {end} {file_path} {temp_path}")
        file_paths.append(temp_path)

    return file_paths
