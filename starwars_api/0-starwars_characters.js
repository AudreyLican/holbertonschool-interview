#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
    console.log('Usage: node print_characters.js <movie_id>');
    process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
    if (error) {
    console.error('Error fetching film:', error);
    return;
    }

    if (response.statusCode !== 200) {
    console.error('Failed to retrieve film data');
    return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

  // Print characters one by one, in order
    function printCharacter(index) {
    if (index >= characters.length) return;

    request(characters[index], (err, res, data) => {
        if (!err && res.statusCode === 200) {
        const character = JSON.parse(data);
        console.log(character.name);
        printCharacter(index + 1); // Recursively call next
        } else {
        console.error('Error fetching character:', err || res.statusCode);
        }
    });
    }

    printCharacter(0);
});
