import torch
import ollama
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import cm
from matplotlib.colors import Normalize

def plot_embeddings(embeddings, labels):
    """
    Plots the embeddings of multiple sentences in a 2D space using PCA for dimensionality reduction.
    Color represents a third dimension mapped from PCA Component 3.
    """
    # Reduce dimensionality to 3D using PCA
    pca = PCA(n_components=3)
    reduced_embeddings = pca.fit_transform(embeddings)

    # Extract PCA components
    x = reduced_embeddings[:, 0]  # First component
    y = reduced_embeddings[:, 1]  # Second component
    z = reduced_embeddings[:, 2]  # Third component for color mapping

    # Normalize z-values for colormap
    norm = Normalize(vmin=np.min(z), vmax=np.max(z))
    colors = cm.viridis(norm(z))  # Use Viridis colormap for third dimension

    # Create scatter plot with correct color mapping
    scatter = plt.scatter(x, y, c=z, cmap="viridis", edgecolors="black", s=100)

    # Annotate points with sentence labels
    for i, label in enumerate(labels):
        plt.text(x[i], y[i], label, fontsize=10, ha='right')

    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title('Sentence Embedding Visualization (Color = PCA Component 3)')

    # Add colorbar correctly
    plt.colorbar(scatter, label="PCA Component 3")

    plt.show()

def get_sentence_embedding(sentence):
    """
    Get embedding for a single sentence using Ollama model.
    """
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=sentence)["embedding"]
    return embedding

def visualize_sentences(sentences):
    """
    Computes embeddings for a list of sentences and visualizes them in a 2D space with color for the third dimension.
    """
    embeddings = []
    labels = []

    # Get embeddings for each sentence
    for sentence in sentences:
        embedding = get_sentence_embedding(sentence)
        embeddings.append(embedding)
        labels.append(sentence)

    # Plot the embeddings of the sentences
    plot_embeddings(embeddings, labels)


# Example usage
sentences = [
    "Planet",
    "Earth",
    "Moon",
    "Sun",
    "Star",
    "Mars",
    "Bread",
    "Cheese",
    "Milk",
    "Hamburger",
    "Mom",
    "Dad",
    "Brother",
    "Sister",
    "Friend",
    "Dead",
    "Mountain", 
    "River", 
    "Ocean",
    "Tree",
    "Flower",
    "Bird",
    "Fish",
    "Sky",
    "Cloud",
    "Rain",
    "Wind",
    "Fire",
    "Lightning",
    "Desert",
    "Forest",
    "Lake",
    "Rock",
    "Cave",
    "Animal",
    "Human",
    "Life",
    "Death",
    "Love",
    "Hate",
    "Fear",
    "Hope",
    "Joy",
    "Sadness",
    "Anger",
    "Peace",
    "War",
    "Victory",
    "Defeat",
    "King",
    "Queen",
    "Prince",
    "Princess",
    "Knight",
    "Dragon",
    "Wizard",
    "Magic",
    "Potion",
    "Spell",
    "Sword",
    "Shield",
    "Armor",
    "Castle",
    "Throne",
    "Empire",
    "Rebel",
    "Soldier",
    "Revolution",
    "Tyrant",
    "Freedom",
    "Justice",
    "Law",
    "Crime",
    "Punishment",
    "Court",
    "Judge",
    "Lawyer",
    "Jail",
    "Prison",
    "Escape",
    "Adventure",
    "Journey",
    "Quest",
    "Treasure",
    "Map",
    "Compass",
    "Key",
    "Lock",
    "Door",
    "Window",
    "Wall",
    "Floor",
    "Ceiling",
    "Room",
    "House",
    "Building",
    "City",
    "Town",
    "Village",
    "Street",
    "Road",
    "Path",
    "Bridge",
    "Tunnel",
    "Train",
    "Car",
    "Bus",
    "Bicycle",
    "Boat",
    "Plane",
    "Ship",
    "Rocket",
    "Astronaut",
    "Alien",
    "Space",
    "Time",
    "Future",
    "Past",
    "Present",
    "Clock",
    "Watch",
    "Calendar",
    "Year",
    "Month",
    "Week",
    "Day",
    "Hour",
    "Minute",
    "Second",
    "Temperature",
    "Heat",
    "Cold",
    "Storm",
    "Snow",
    "Frost",
    "Ice",
    "Mud",
    "Dirt",
    "Sand",
    "Dust",
    "Rock",
    "Gem",
    "Diamond",
    "Gold",
    "Silver",
    "Copper",
    "Iron",
    "Steel",
    "Wood",
    "Paper",
    "Plastic",
    "Glass",
    "Stone",
    "Clay",
    "Fabric",
    "Thread",
    "Needle",
    "Scissors",
    "Tape",
    "Glue",
    "Paint",
    "Brush",
    "Canvas",
    "Picture",
    "Photo",
    "Camera",
    "Film",
    "Music",
    "Song",
    "Dance",
    "Instrument",
    "Guitar",
    "Piano",
    "Drum",
    "Violin",
    "Flute",
    "Trumpet",
    "Saxophone",
    "Concert",
    "Festival",
    "Theater",
    "Play",
    "Movie",
    "Actor",
    "Director",
    "Producer",
    "Screenplay",
    "Studio",
    "Script",
    "Rehearsal",
    "Audition",
    "Performance",
          
]

visualize_sentences(sentences)
