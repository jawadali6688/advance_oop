// 
// router.post('/search_by_image', upload.single('image'), (req, res) => {
//   try {
//     // Check if file is uploaded
//   if (!req.file) {
//     return res.status(400).json({ error: 'No file uploaded' });
//   }

//   // Ensure the uploads directory exists
//   const uploadsDir = path.join(__dirname, 'uploads');
//   if (!fs.existsSync(uploadsDir)) {
//     fs.mkdirSync(uploadsDir, { recursive: true });
//   }

//   // Define file paths
//   const excelFilePath = path.join(__dirname, '1733160801682-fffff.xlsx');
//   const tempFilePath = path.join(uploadsDir, req.file.originalname);

//   // Save uploaded file to disk
//   fs.writeFile(tempFilePath, req.file.buffer, (err) => {
//     if (err) {
//       console.error('Error saving file to disk:', err);
//       return res.status(500).json({ error: 'Failed to save the uploaded file' });
//     }

//     const pythonScriptPath = path.join(__dirname, 'image_search.py');

//     // Execute the Python script
//     const command = `python "${pythonScriptPath}" --query_img "${tempFilePath}" --excel_file "${excelFilePath}"`;
//     exec(command, (err, stdout, stderr) => {
//       // Delete the temporary file
//       fs.unlink(tempFilePath, (unlinkErr) => {
//         if (unlinkErr) console.error('Error deleting temporary file:', unlinkErr);
//       });

//       if (err) {
//         console.error('Error executing Python script:', stderr || err.message);
//         return res.status(500).json({ error: 'Error processing image' });
//       }
//       console.log(stdout, "all data")
//       try {
//         // Parse Python script output
//         res.json({ relatedImages: stdout });
//       } catch (parseError) {
//         console.error('Error parsing Python script output:', stderr || stdout);
//         res.status(500).json({ error: 'Invalid output from script' });
//       }
//     });
//   });
//   } catch (error) {
//     console.log(error)
//   }
// });