const alertBox = document.getElementById('alert-box');
const form = document.getElementById('contact-form');
const title = document.getElementById('id_title');
const fName = document.getElementById('id_firstName');
const lName = document.getElementById('id_lastName');
const emailAddress = document.getElementById('id_email');
const desc = document.getElementById('id_description');
const csrf = document.getElementsByName('csrfmiddlewaretoken');
const url = '';

const titleErrMsg = document.getElementById('title-error-message');
const fNameErrMsg = document.getElementById('fname-error-message');
const lNameErrMsg = document.getElementById('lname-error-message');
const descErrMsg = document.getElementById('desc-error-message');
const submitBtn = document.getElementById('submit-btn');

const handleSubmitAlerts = (type, text) => {
  alertBox.innerHTML = `
  <div class="mt-5">
    <span class="${type}">${text}</span>
  </div>
  `
};

$(document).ready(function () {
  $(form).submit(function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrf[0].value);
    formData.append('title', title.value);
    formData.append('firstName', fName.value);
    formData.append('lastName', lName.value);
    formData.append('email', emailAddress.value);
    formData.append('description', desc.value);

    function successSubmit() {
      form.reset();
      const type = 'text-successGreen text-lg font-medium';
      const text = 'Submitted successfully!';
      handleSubmitAlerts(type, text);
      setTimeout(() => {
        alertBox.innerHTML = "";
      }, 5000);
    }

    function errorSubmit() {
      form.reset();
      const type = 'text-red-600 text-lg font-medium';
      const text = 'Submission failed! If you are unable to submit your data, please contact us directly!';
      handleSubmitAlerts(type, text);
      setTimeout(() => {
        alertBox.innerHTML = "";
      }, 5000);
    }

    $.ajax({
      type: 'POST',
      url: url,
      header: { 'X-CSRFToken': csrf },
      data: formData,
      success: function (data) {
        console.log(data.status);
        if (data.status.result === 'failed') {
          checkTitle();
        } else {
          successSubmit();
          $('#title-error-message').hide();
        }
      },
      error: function (error) {
        console.log(error);
        errorSubmit();
      },
      cache: false,
      contentType: false,
      processData: false
    })
  });

  ////////////////////
   /// validations ///
   //////////////////

  const errorTitleTemp = (type, text) => {
    titleErrMsg.innerHTML = `
    <div class="my-2">
        <span class="${type}">${text}</span>
    </div>
    `
  }

  $('#title-error-message').hide();
  var errTitle = false;

  function checkTitle() {
    let letterPattern = /^[a-zA-Z]*$/; // /^[a-zA-Z\s]*$/; - with spaces ===> (\s)
    let t = $(title).val();
    let titleLength = $(title).val().length;
    const numOfChars = 5;
    if (!letterPattern.test(t)) {
        const type = 'text-red-600 text-sm font-normal';
        const text = 'The title should contain only characters';
        errorTitleTemp(type, text);
        $('#title-error-message').show();
        errTitle = true;
    } else if (titleLength < numOfChars) {
        const type = 'text-red-600 text-sm font-normal';
        const text = 'The title should be at least five characters long';
        errorTitleTemp(type, text);
        $('#title-error-message').show();
        errTitle = true;
    } else {
        $('#title-error-message').hide();
    }
  };
});