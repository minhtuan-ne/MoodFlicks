# Mood Flicks

<p align="center">
  <img src="/images-for-readme/page1.jpg" alt="Image 1" width="200">
  <img src="/images-for-readme/page2.jpg" alt="Image 2" width="200">
  <img src="/images-for-readme/page3.jpg" alt="Image 3" width="200">
  <img src="/images-for-readme/page4.jpg" alt="Image 4" width="200">
</p>

## Description

Mood Flicks is a web application that recommends movies based on the user's current mood and time of day. Built with Flask, it integrates The Movie Database (TMDB) API to provide personalized movie suggestions.
This project is inspired by Marc Lou's Mood2Movie.

## Features

- User input for mood and time of day
- Movie recommendations based on user input
- Display of movie details including title, release date, genres, and description

## Technologies Used

- Python
- Flask
- SQLite
- HTML/CSS
- Bootstrap
- JavaScript
- TMDB API

## Installation

1. Clone the repository:
   git clone https://github.com/minhtuan-ne/MoodFlicks.git
2. Navigate to the project directory:
   cd mood-flicks
3. Install required packages:
   pip install -r requirements.txt
4. Set up your TMDB API key:

- Sign up for an account at [https://www.themoviedb.org/](https://www.themoviedb.org/)
- Get your API key from your account settings
- Create a .env file and insert your TMDB_API_KEY = 'here_is_your_api_key'

## Usage

1. Run the Flask application:
   python app.py
2. Open a web browser and go to `http://localhost:8000`
3. Select your time of day and mood
4. Browse through movie recommendations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

- [The Movie Database (TMDB)](https://www.themoviedb.org/) for providing the movie data API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for the frontend framework
- [Mood2Movie](https://mood2movie.com/) for the idea
