<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="./logo.jpeg" alt="Logo" width="80">

  <h3 align="center">Photo To Pixels</h3>

  <p align="center">
   Transform an image into a dataset of RGB values
  </p>
</p>

<!-- ABOUT THE PROJECT -->

## About The Project

Apart of my NSF Research project, I was tasked with taking images of the sky
and creating a dataset of RGB values. In the Version 1, for each image, I had
to create 25 10x10 patches, then add the rgb values for each pixel in the 10x10 to
an excel sheet. In a seperate program, I attached turbidity values to the end
of each row of data. In Version 2, for each pixel, I calculated a ratio of Blue/Green
and created a new dataset with those ratio values. Again, the turbidity values
were appended to the end of each row.

Testing a pull request.

### Built With

- [Pillow](https://python-pillow.org/)
- [Pandas](https://pandas.pydata.org/)

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- python3.8

  ```sh
  sudo apt update
  sudo apt install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt install python3.8
  ```

- pip3
  ```sh
  sudo apt install python3-pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/michaelnavs/pixelize.git
   ```
2. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
3. Activate virtual environmnt
   ```sh
   source venv/bin/activate
   ```
4. Install required packages

   ```sh
   pip install -r requirements.txt
   ```

5. Run the program
   ```
   python main.py
   ```
