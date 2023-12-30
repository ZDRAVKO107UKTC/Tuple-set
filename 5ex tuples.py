total_invitations = int(input())
invitations_set = set(input() for _ in range(total_invitations))

arrived_guests = set()

while True:
    invitation = input()
    if invitation == "END":
        break

    arrived_guests.add(invitation)

missing_guests = invitations_set - arrived_guests

print(len(missing_guests))
print("\n".join(sorted(missing_guests, key=lambda x: (x[0].isdigit(), x))))
