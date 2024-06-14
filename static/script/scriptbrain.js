const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");
const predictionText = document.getElementById("PredictionText")
const imgPreview = document.getElementById("img-preview")

inputFile.addEventListener("change",uploadImage)
{
//   //  Check if a file is selected
//    if (inputFile.files && inputFile.files[0]) {
//     // Get the selected file
//     const file = inputFile.files[0];
//     // Display the image preview
//     imgPreview.style.display = "block";
//     imgPreview.src = URL.createObjectURL(file);
// }
};

// function uploadImage(){
//     let imgLink = URL.createObjectURL(inputFile.files[0]);
//     imageView.style.backgroundImage= `url(${imgLink})`;
//     imageView.textContent="";
//     imageView.style.border="none";
//     const xhr = new XMLHttpRequest();
//     xhr.open('POST', '/predict', true);
//     xhr.onreadystatechange = function() {
//       if (xhr.readyState === XMLHttpRequest.DONE) {
//         if (xhr.status === 200) {
//           const serverPrediction = xhr.responseText;
//           predictionText.textContent = `Prediction: Rs ${serverPrediction}`;
//         } else {
//           console.error('Error sending image to server');
//           predictionText.textContent = 'Prediction failed';
//         }
//       }
//     };

//     const formData = new FormData();
//     formData.append('image',  imgLink);
//     xhr.send(formData);
  
//   };


dropArea.addEventListener("dragover",function(e){
    e.preventDefault();
});

dropArea.addEventListener("drop",function(e){
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
});


function uploadImage() {
  const file = inputFile.files[0]; // Get the selected file
  const formData = new FormData(); // Create FormData object
  formData.append('image', file); // Append the file to FormData


    // Display image preview
  // const imgLink = URL.createObjectURL(file);
  // imageView.style.backgroundImage = `url(${imgLink})`;
  // imageView.textContent = "";
  // imageView.style.border = "none";

  // const imgLink = URL.createObjectURL(file);
  // imageView.style.backgroundImage = `url(${imgLink})`;
  // imageView.style.width = "200px"; // Set width to 200 pixels
  // imageView.style.height = "150px"; // Set height to 150 pixels
  // imageView.style.backgroundSize = "cover"; // Adjust size to cover the entire element
  // imageView.textContent = "";
  // imageView.style.border = "none";

  const imgLink = URL.createObjectURL(file);
  imageView.style.backgroundImage = `url(${imgLink})`;
  imageView.style.backgroundSize = "contain"; // Adjust size to contain the entire image
  imageView.textContent = "";
  imageView.style.border = "none";
  imageView.style.backgroundRepeat = "no-repeat"; // Prevent image from repeating

    fetch('/predictbrain', {
      method: 'POST',
      body: formData
    })

    .then(response => response.json())  // Parse JSON response
    .then(data => {
      if (data.error) {
        console.error(data.error);

        predictionText.textContent = "Error: " + data.error;
      } else {
        
        document.getElementById('PredictionText').textContent = data.prediction;
        document.getElementById('extra').textContent = data.extra;
      }
    })
    .catch(error => {
      console.error(error);
      predictionText.textContent = "Error: " + error;
    });
}



