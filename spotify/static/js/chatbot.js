$(document).ready(function () {
  function handleSubmit() {
    var userInput = $("#userInput").val();

    $.ajax({
      type: "POST",
      url: "get_openai_answer",
      data: {
        userInput: userInput,
        csrfmiddlewaretoken: "{{ csrf_token }}", // Include CSRF token
      },
      success: function (data) {
        $("#chat ul").append(
          // "<li class='list-group-item' style='text-align: right; background-color: #c0b8b8; border-radius: 8px; padding: 10px;'>" +
          //   userInput +
          //   "</li>"

          "<li class='list-group-item' style='text-align: right; padding: 10px; border: none;'>" +
          "<span style='display: inline-block; background-color: #c0b8b8; border-radius: 8px; padding: 10px; max-width: 500px;'>" +
          userInput +
          "</span>" +
          "</li>"
        );
        $("#chat ul").append(
          "<li class='list-group-item'><b>Answer:</b> " +
          data.completion +
          "</li>"
        );
        $("#userInput").val(""); // Clear the input field
      },
      error: function (xhr, status, error) {
        console.error("Error: " + error);
        $("#chat ul").append(
          "<li class='list-group-item text-danger'><b>Error:</b> Could not get a response.</li>"
        );
      },
    });
  }

  // Event listener for the submit button click
  $("#submit").click(function () {
    handleSubmit();
  });

  // Event listener for the Enter key press
  $("#userInput").keydown(function (event) {
    if (event.key === "Enter") {
      event.preventDefault(); // Prevent the default form submission behavior
      handleSubmit();
    }
  });
});