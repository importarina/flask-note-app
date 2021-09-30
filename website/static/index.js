function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/"; // redirects us to the homepage
    });
}