import secrets

def generate_meeting_link():
    room_id = secrets.token_hex(4)
    meeting_link = f"https://example.com/join/{room_id}"
    return meeting_link

if __name__ == "__main__":
    meeting_link = generate_meeting_link()
    print(meeting_link)
