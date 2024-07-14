# Driver-Customer Mapping Project

## Overview
Driver-Customer Mapping with H3 Geospatial Indexing

Explore the power of H3 geospatial indexing in a practical application for mapping drivers and customers dynamically. Inspired by real-world logistics solutions like Uber, this project utilizes H3's hexagonal grid system to efficiently match customers with the nearest drivers based on both H3 indexing and geodesic distance calculations.

## H3 Hexagonal Hierarchical Spatial Indexing
[H3](https://eng.uber.com/h3/) is a powerful open-source library developed by Uber for spatial indexing. It divides the Earth's surface into hexagonal cells of various resolutions, allowing efficient indexing, clustering, and querying of geospatial data.

## Project Setup
To run this project locally, follow these steps:

### Prerequisites
- Python 3.x installed
- Virtualenv installed (optional but recommended)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Nik-luftmensch/driver-customer-mapping
   cd driver-customer-mapping
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
To run the project:

1. Run tests:
   ```bash
   make test
   ```

2. Execute the main project script:
   ```bash
   make run
   ```

### Output
The main script will generate an interactive map (`map_advanced.html`) showing the customer's location, nearest driver, and route between them.

You can view the generated map here: [View Map HTML](./map_advanced.html) or [View Map Img](./Output_Map.png)

## References
- [Uber Engineering Blog on H3](https://eng.uber.com/h3/)
- [H3 Documentation](https://h3geo.org/docs/)

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.