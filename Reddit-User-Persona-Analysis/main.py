import praw
import os
from collections import defaultdict

# ==== STEP 1: Set up Reddit API credentials ====
client_id = "ExfbNnNKtqBI6oP3lZontg"
client_secret = "7MU9mA3VosKbJp9mcSG6rr7dSG-Oeg"
user_agent = "script:reddit-persona:v1.0 (by u/FriendshipOk6460)"

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# ==== STEP 2: Input Reddit username ====
profile_url = input("Enter Reddit profile URL: ").strip()
username = profile_url.rstrip('/').split('/')[-1]
redditor = reddit.redditor(username)

# ==== STEP 3: Scrape posts and comments ====
posts = []
comments = []
subreddits = []

print(f"🧠 Posts by u/{username}:")
for post in redditor.submissions.new(limit=10):
    posts.append(post.title + " " + (post.selftext or ""))
    subreddits.append(str(post.subreddit))
    print(f"➤ {post.title}")

print(f"\n💬 Comments by u/{username}:")
for comment in redditor.comments.new(limit=15):
    comments.append(comment.body)
    subreddits.append(str(comment.subreddit))
    print(f"➤ {comment.body[:100]}...")

# Save raw data for reference
os.makedirs("output", exist_ok=True)
with open(f"output/{username}_raw.txt", "w", encoding="utf-8") as f:
    f.write("=== POSTS ===\n")
    f.write("\n---\n".join(posts))
    f.write("\n\n=== COMMENTS ===\n")
    f.write("\n---\n".join(comments))

print(f"✅ Saved user posts and comments to 'output/{username}_raw.txt'")

# ==== STEP 6: Build User Persona ====

# Step 6.1–6.4 Combined
all_text = " ".join(posts + comments).lower()
traits = defaultdict(list)

traits["Username"] = [username]

if "university" in all_text or "graduated" in all_text or "college" in all_text:
    traits["Education"].append("Mentions higher education or graduation.")

if any(word in all_text for word in ["python", "java", "developer", "engineer", "coding", "software"]):
    traits["Profession/Skills"].append("Shows interest in tech or software development.")

if any(word in all_text for word in ["funny", "meme", "lol", "haha", "joke"]):
    traits["Personality"].append("Enjoys humor and memes.")

if "i believe" in all_text or "in my opinion" in all_text or "i think" in all_text:
    traits["Beliefs"].append("Shares strong personal opinions.")

if any(word in all_text for word in ["help", "suggest", "advice", "support"]):
    traits["Tone"].append("Helpful and community-driven.")

traits["Subreddits Active In"] = list(set(subreddits))

# Add citations from comments
for comment in comments:
    body = comment.lower()
    if "university" in body or "graduated" in body:
        traits["Education"].append(f'Snippet: "{comment[:100]}..."')
    if "python" in body:
        traits["Profession/Skills"].append(f'Snippet: "{comment[:100]}..."')
    if "funny" in body or "meme" in body:
        traits["Personality"].append(f'Snippet: "{comment[:100]}..."')
    if "i believe" in body or "i think" in body:
        traits["Beliefs"].append(f'Snippet: "{comment[:100]}..."')

# Save persona to text file
persona_path = os.path.join("output", f"{username}.txt")
with open(persona_path, "w", encoding="utf-8") as f:
    f.write(f"👤 Reddit Persona: u/{username}\n\n")
    for trait, values in traits.items():
        f.write(f"📌 {trait}:\n")
        for value in set(values):
            f.write(f"- {value}\n")
