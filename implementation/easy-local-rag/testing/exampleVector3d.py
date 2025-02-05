import torch
import ollama
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import Normalize

def plot_4d_embeddings(embeddings, labels):
    """
    Plots embeddings in a 3D space with color representing a fourth dimension (PCA Component 4).
    """
    # Reduce dimensionality to 4D using PCA
    pca = PCA(n_components=4)
    reduced_embeddings = pca.fit_transform(embeddings)

    # Extract PCA components
    x = reduced_embeddings[:, 0]  # First component (X-axis)
    y = reduced_embeddings[:, 1]  # Second component (Y-axis)
    z = reduced_embeddings[:, 2]  # Third component (Z-axis)
    c = reduced_embeddings[:, 3]  # Fourth component (color)

    # Normalize color values
    norm = Normalize(vmin=np.min(c), vmax=np.max(c))
    colors = cm.viridis(norm(c))  # Use colormap for fourth dimension

    # Create 3D scatter plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot with color mapped from the fourth PCA component
    scatter = ax.scatter(x, y, z, c=c, cmap="viridis", edgecolors="black", s=100)

    # Annotate points with sentence labels
    for i, label in enumerate(labels):
        ax.text(x[i], y[i], z[i], label, fontsize=10)

    # Labels and title
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')
    ax.set_zlabel('PCA Component 3')
    ax.set_title('4D Sentence Embedding Visualization (Color = PCA Component 4)')

    # Add colorbar
    fig.colorbar(scatter, ax=ax, label="PCA Component 4")

    # Show plot
    plt.show()

def get_sentence_embedding(sentence):
    """
    Get embedding for a single sentence using Ollama model.
    """
    embedding = ollama.embeddings(model='mxbai-embed-large', prompt=sentence)["embedding"]
    return embedding

def visualize_sentences_4d(sentences):
    """
    Computes embeddings for a list of sentences and visualizes them in a 3D space with color as a fourth axis.
    """
    embeddings = []
    labels = []

    # Get embeddings for each sentence
    for sentence in sentences:
        embedding = get_sentence_embedding(sentence)
        embeddings.append(embedding)
        labels.append(sentence)

    # Plot the embeddings with 4D representation
    plot_4d_embeddings(embeddings, labels)

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

visualize_sentences_4d(sentences)
