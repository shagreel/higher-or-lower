# higher-or-lower
A simple javascript statistical game created for use at an elementary school STEM night. [Try the demo](https://shagreel.github.io/higher-or-lower/highorlow.html).

In this game you start with a shuffled deck of 10 cards, Ace through 10. The first card is dealt face up. You then must determine if the next card will be higher or lower than the last card. This allows students to learn basic statistical probablility.

This repo contains a small python script which runs the game automatically millions of times using the best possible guesses to determine the expected probability of winning. The overall probablity of winning the game is around 12%. 

I gave the following to the students to get them started.

Higher or Lower?

Statistics is a math game that tries to explain why things happen in our world. Statistics can use math to guess what will happen in the future. In this game you will try flip over the top card of a deck of cards one at a time and try to guess if the next card will be higher or lower than the last card. You can use the chart below to help you guess what the next card will be.
1. Get a deck of cards with only the numbers 1-10.
2. Flip over the first card.
3. Guess if the next card will be higher or lower than the card showing.
4. Flip over the next card and see if you are correct.
5. Keep doing this until you are wrong.

How can statistics help you? When you are looking at a card, count how many numbers are less than the card showing and count how many numbers are greater than the card showing. Whichever one has more tells you what to guess. For example, if you are looking at a 2, there is only 1 number lower than a 2, but there are 8 numbers higher than a 2. So you should guess “higher”.

What number is showing?
How many are higher?
How many are lower?
Play the game until you get the hang of it. Can you guess right every time? Then you can challenge statistics and see if you can outguess the math.

Special thanks to [Danny Engelman](https://github.com/Danny-Engelman) for the [card
 meister library](https://cardmeister.github.io/) and [Felix Krause](https://github.com/efkah) for the [sparkle library](https://github.com/efkah/sparkle.js).