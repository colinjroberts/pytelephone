# pytelephone

A python bsaed implementation of the game telephone.

## General Idea

In the game of telephone, a group of people sit in a circle. One person whispers a message to another person. That person whispers is to the next and the next and so on until the message finally arrives at the person who said it. In many cases, the message will have mutated from the original, often in humorous ways.

This program should be able to record a sample of of a person talking, slightly alter the message an arbitrary number of times, then use computer generated speech to say the final mutated message.

## Steps

- [done] Use vosk module to parse recordings. (https://github.com/alphacep/vosk-api)
- Use PyDictionary module to replace one word with a synonym an arbitrary number of times.
- Find some way of converting text to speech that doesn't sound terrible.

## Installation

- Getting PocketSphinx on OSX was a bit of a pain. Resolved with `https://github.com/bambocher/pocketsphinx-python/issues/28#issuecomment-334493324` and the comments underneath that suggesting:

```
brew install swig
pip install git+https://github.com/oyeun/pocketsphinx-python/
```
