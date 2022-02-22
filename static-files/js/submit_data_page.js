const alertBox = document.getElementById('alert-box');
const form = document.getElementById('p-form');
const title = document.getElementById('id_title');
const fName = document.getElementById('id_firstName');
const lName = document.getElementById('id_lastName');
const emailAddress = document.getElementById('id_email');
const desc = document.getElementById('id_description');
const subFile = document.getElementById('id_submitFile');
const csrf = document.getElementsByName('csrfmiddlewaretoken');
const url = '';

const titleErrMsg = document.getElementById('title-error-message');
const fNameErrMsg = document.getElementById('fname-error-message');
const lNameErrMsg = document.getElementById('lname-error-message');
const emailErrMsg = document.getElementById('email-error-message');
const descErrMsg = document.getElementById('desc-error-message');
const subFileSizeErrMsg = document.getElementById('subFile-error-size-message');
const subFileExtErrMsg = document.getElementById('subFile-error-ext-message');
const subFileMimeErrMsg = document.getElementById('subFile-error-mime-message');
const submitBtn = document.getElementById('submit-btn');

const handleSubmitAlerts = (type, text) => {
   alertBox.innerHTML = `
   <div class="mt-5">
      <span class="${type}">${text}</span>
   </div>
   `
}

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
      formData.append('submitFile', subFile.files[0]);

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
         enctype: 'multipart/form-data',
         header: { 'X-CSRFToken': csrf },
         data: formData,
         success: function (data) {
            console.log(data.status);
            if (data.status.result === 'failed') {
               checkTitle();
               checkFirstName();
               checkLastName();
               // checkEmail();
               checkDesc();
               checkFileSize();
               checkFileExtension();
               // checkFileMime();
               // checkEmptyStringFields();
            } else {
               successSubmit();
               $('#title-error-message').hide();
               $('#fname-error-message').hide();
               $('#lname-error-message').hide();
               // $('#email-error-message').hide();
               $('#desc-error-message').hide();
               $('#subFile-error-size-message').hide();
               $('#subFile-error-ext-message').hide();
               // $('#subFile-error-mime-message').hide();
            }
         },
         error: function (error) {
            console.log(error);
            errorSubmit();
         },
         cache: false,
         contentType: false,
         processData: false,
      });
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

   const errorFirstNameTemp = (type, text) => {
      fNameErrMsg.innerHTML = `
      <div class="my-2">
         <span class="${type}">${text}</span>
      </div>
      `
   }

   const errorLastNameTemp = (type, text) => {
      lNameErrMsg.innerHTML = `
      <div class="my-2">
         <span class="${type}">${text}</span>
      </div>
      `
   }

   const errorEmailTemp = (type, text) => {
      emailErrMsg.innerHTML = `
      <div class="my-2">
         <span class="${type}">${text}</span>
      </div>
      `
   }

   const errorDescTemp = (type, text) => {
      descErrMsg.innerHTML = `
      <div class="my-2">
         <span class="${type}">${text}</span>
      </div>
      `
   }

   const errorsFileSize = (type, text) => {
      subFileSizeErrMsg.innerHTML = `
      <div class="my-5">
         <span class="${type}">${text}</span>
      </div>
      `
   }

   const errorsFileExt = (type, text) => {
      subFileExtErrMsg.innerHTML = `
      <div class="my-5">
         <span class="${type}">${text}</span>
      </div>
      `
   }

   // const errorsFileMime = (type, text) => {
   //    subFileMimeErrMsg.innerHTML = `
   //    <div class="my-5">
   //       <span class="${type}">${text}</span>
   //    </div>
   //    `
   // }

   $('#title-error-message').hide();
   var errTitle = false;

   $('#fname-error-message').hide();
   var errFirstName = false;

   $('#lname-error-message').hide(); 
   var errLastName = false;

   $('#email-error-message').hide();
   var errEmail = false;

   $('#desc-error-message').hide();
   var errDesc = false;

   $('#subFile-error-size-message').hide();
   var errFileSubSize = false;

   $('#subFile-error-ext-message').hide();
   var errFileSubExt = false;

   // $('#subFile-error-mime-message').hide();
   // var errFileSubMime = false;

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

   function checkFirstName() {
      let letterPattern = /^[a-zA-Z]*$/;
      let fN = $(fName).val();
      let fNameLength = $(fName).val().length;
      const numOfChars = 2;
      if (!letterPattern.test(fN)) {
         const type = 'text-red-600 text-sm font-normal';
         const text = 'The first name should contain only characters';
         errorFirstNameTemp(type, text);
         $('#fname-error-message').show();
         errFirstName = true;
      } else if (fNameLength < numOfChars) {
         const type = 'text-red-600 text-sm font-normal';
         const text = 'The first name should be at least two characters long';
         errorFirstNameTemp(type, text);
         $('#fname-error-message').show();
         errFirstName = true;
      } else {
         $('#fname-error-message').hide();
      }
   };

   function checkLastName() {
      let letterPattern = /^[a-zA-Z]*$/;
      let lN = $(lName).val();
      let lNameLength = $(lName).val().length;
      const numOfChars = 2;
      if (!letterPattern.test(lN)) {
         const type = 'text-red-600 text-sm font-normal';
         const text = 'The last name should contain only characters';
         errorLastNameTemp(type, text);
         $('#lname-error-message').show();
         errLastName = true;
      } else if (lNameLength < numOfChars) {
         const type = 'text-red-600 text-sm font-normal';
         const text = 'The last name should be at least two characters long';
         errorLastNameTemp(type, text);
         $('#lname-error-message').show();
         errLastName = true;
      } else {
         $('#lname-error-message').hide();
      }
   };

   // function checkEmail() {
   //    let emailLettersPattern = /^([a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z])+$/; // /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/; 
   //    let eA = $(emailAddress).val();
   //    let emailLength = $(emailAddress).val().length;
   //    const numOfChars = 0;
   //    if (!emailLettersPattern.test(eA)) {
   //       const type = 'text-red-600 text-sm font-normal';
   //       const text = 'Invalid email address format';
   //       errorEmailTemp(type, text);
   //       $('#email-error-message').show();
   //       errEmail = true;
   //    } else if (emailLength === numOfChars) {
   //       const type = 'text-red-600 text-sm font-normal';
   //       const text = 'You forgot to type in your email';
   //       errorEmailTemp(type, text);
   //       $('#email-error-message').show();
   //       errEmail = true;
   //    } else {
   //       $('#email-error-message').hide();
   //    }
   // };

   function checkDesc() {
      let descLength = $(desc).val().length;
      const numOfChars = 5;
      if (descLength < numOfChars) {
         const type = 'text-red-600 text-sm font-normal';
         const text = 'The description should be at least five characters long';
         errorDescTemp(type, text);
         $('#desc-error-message').show();
         errDesc = true;
      } else {
         $('#desc-error-message').hide();
      }
   };

   function checkFileSize() {
      $('#subFile-error-size-message').html('');
      var fs = $(subFile)[0].files[0].size;
      var s = 10485760; // 10MB
      if (fs > s) {
         const type = 'text-red-600 text-sm font-normal';
         const text = 'File size is greater than 10MB. Please, upload the file with a smaller size';
         errorsFileSize(type, text);
         $('#subFile-error-size-message').show();
         errFileSubSize = true;
      } else {
         $('#subFile-error-size-message').hide();
      } 
   }

   function checkFileExtension() {
      var filePath = subFile.value;
      var ext = /(\.docx|\.DOCX|\.pdf|\.PDF|\.jpeg|\.JPEG|\.png|\.PNG|\.xlsx|\.XLSX|\.xls|\.XLS|\.txt|\.TXT|\.jpg|\.JPG|\.zip|\.ZIP|\.rar|\.RAR)$/;
      if (filePath != "" && !ext.exec(filePath)) {
         const type = 'text-red-600 text-sm font-normal';
         const text = 'Please upload a file with a valid extension';
         errorsFileExt(type, text);
         $('#subFile-error-ext-message').show();
         errFileSubExt = true;
      } else {
         $('#subFile-error-ext-message').hide();
      }
   }

   // function checkFileMime() {
   //    let output = $(subFileMimeErrMsg);
   //    if (window.FileReader && window.Blob) {
   //       $(submitBtn).click(function () {
   //          let fls = $(subFile).get(0).files;
   //          if (fls.length > 0) {
   //             let file = fls[0];
   //             console.log('Loaded file: ' + file.name);
   //             console.log('Blob mime: ' + file.type);
   //             let fileReader = new FileReader();
   //             fileReader.onloadend = function (e) {
   //                let arr = (new Uint8Array(e.target.result)).subarray(0, 4);
   //                let header = '';
   //                for (let i = 0; i < arr.length; i++) {
   //                   header += arr[i].toString(16);
   //                }
   //                // console.log('File header: ' + head);

   //                // file types
   //                // ['.pdf', '.docx', '.jpg', '.jpeg', '.png', '.xlsx', '.xls', '.txt']
   //                let type = 'unknown';
   //                switch (header) {
   //                   case '255044462D312E':
   //                      type = 'application/pdf'; // pdf
   //                      break;
   //                   case '504B030414000600':
   //                      type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'; // docx
   //                      break;
   //                   case '504B030414000600':
   //                      type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'; // xlsx
   //                      break;
   //                   case 'FFD8FFE2':
   //                   case 'FFD8FFE0':
   //                   case 'FFD8FFE1':
   //                      type = 'image/jpeg'; // jpeg
   //                      break;
   //                   case '89504E47':
   //                      type = 'image/png'; // png
   //                      break;
   //                   case 'FFD8FF':
   //                      type = 'jpg'; // jpg
   //                      break;
   //                   case 'D0CF11E0':
   //                      type = 'application/vnd.ms-excel'; // xls
   //                      break;
   //                   case '504B0304':
   //                      type = 'application/zip'; // zip folder
   //                      break;
   //                   case '52617221':
   //                      type = 'application/vnd.rar'; // rar folder
   //                      break;
   //                   case 'EFBBBF':
   //                      type = 'text/plain'; // txt
   //                      break;
   //                }
   //                if (file.type !== type) {
   //                   const type = 'text-red-600 text-sm font-normal';
   //                   const text = 'Invalid file type. Please try again';
   //                   output = errorsFileMime(type, text);
   //                   $('#subFile-error-mime-message').show();
   //                   errFileSubMime = true;
   //                } else {
   //                   $('#subFile-error-mime-message').hide();
   //                }
   //             };
   //             fileReader.readAsArrayBuffer(file);
   //          }
   //       });
   //    } 
   // }
});
