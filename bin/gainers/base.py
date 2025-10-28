from abc import abstractmethod
class GainerBase():
    def __init__(self):
        pass

    @abstractmethod
    def download_html(self):
        """Download the raw HTML to a file."""
        pass

    @abstractmethod
    def extract_csv(self):
        """Parse the saved HTML into a CSV file."""
        pass

    @abstractmethod
    def normalize_data(self):
        """Normalize the CSV columns and write a standardized CSV."""
        pass
