from graphviz import Digraph

# Create the diagram
dot = Digraph(comment="Tutoring & Peer Help Matching System", format="png")
dot.attr(rankdir="LR", fontsize="10")

# Entities with attributes
entities = {
    "User": ["id", "email", "password", "first_name", "last_name"],
    "Profile": ["id", "school", "program", "year_level", "phone"],
    "TutorProfile": ["id", "hourly_rate", "bio", "rating_avg"],
    "Subject": ["id", "name", "code"],
    "Availability": ["id", "start", "end", "is_recurring"],
    "Booking": ["id", "start_time", "end_time", "status", "price"],
    "Review": ["id", "rating", "comment"],
    "Message": ["id", "body", "sent_at"],
    "Payment": ["id", "amount", "status", "paid_at"],
    "Payout": ["id", "amount", "status", "requested_at"],
    "Notification": ["id", "type", "title", "body"]
}

# Add nodes
for entity, fields in entities.items():
    label = entity + "|" + "\\l".join(fields) + "\\l"
    dot.node(entity, label=label, shape="record")

# Relationships
dot.edge("User", "Profile", label="1:1")
dot.edge("User", "TutorProfile", label="1:0..1")
dot.edge("TutorProfile", "Availability", label="1:N")
dot.edge("TutorProfile", "Booking", label="1:N (as_tutor)")
dot.edge("User", "Booking", label="1:N (as_student)")
dot.edge("Booking", "Review", label="1:0..1")
dot.edge("TutorProfile", "Review", label="1:N")
dot.edge("Booking", "Subject", label="N:1")
dot.edge("TutorProfile", "Subject", label="M:N")
dot.edge("Booking", "Message", label="1:N")
dot.edge("User", "Message", label="1:N")
dot.edge("Booking", "Payment", label="1:0..1")
dot.edge("User", "Payout", label="1:N")
dot.edge("User", "Notification", label="1:N")

# Render to file
file_path = "/mnt/data/tutoring_system_class_diagram"
dot.render(file_path)

file_path + ".png"
