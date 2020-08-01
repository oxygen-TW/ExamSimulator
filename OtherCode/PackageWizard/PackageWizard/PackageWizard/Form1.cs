using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;
using System.Drawing.Imaging;
using Tommy;
using System.IO;
using System.IO.Compression;

namespace PackageWizard
{
    public partial class Form1 : Form
    {

        String ImagePath = "";
        String Ans = "";
        String FolderPath = "test";
        Int32 counter = 1;
        TomlTable TomlT;
        Image imageShow;

        public Form1()
        {
            InitializeComponent();
        }

        public void SaveTOML(TomlTable Data)
        {

            using (StreamWriter writer = new StreamWriter(File.OpenWrite(FolderPath + "\\config.toml")))
                Data.ToTomlString(writer);
        }

        private void FileImportLable_DragDrop(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.All;//调用DragDrop事件 
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }

        private void FileImportLable_DragEnter(object sender, DragEventArgs e)
        {
            string[] filePaths = (string[])e.Data.GetData(DataFormats.FileDrop);
            ImagePath = filePaths[0];

            Image image1 = Image.FromFile(ImagePath);
            ImageFormat format = image1.RawFormat;

            int width = 800; //寬度
            int heigt = 600; //高度
            Bitmap imgoutput = new Bitmap(image1, width, heigt); //輸出一個新圖片
            imgoutput.Save("tmp.jpg", format); //存檔路徑,格式

            imgoutput.Dispose();
            image1.Dispose();

            imageShow = Image.FromFile("tmp.jpg");
            FileImportLable.Image = imageShow;

        }

        private void WriteBtn_Click(object sender, EventArgs e)
        {
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            TomlT = new TomlTable
            {
                ["title"] = "TOML Example",
                ["answer"] = { }

            };

            /*if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                FolderPath = folderBrowserDialog1.SelectedPath;
                Console.Write(FolderPath);
                PathtoolStripLabel.Text = FolderPath;
            }*/

            // Determine whether the directory exists.
            /*if (!Directory.Exists(FolderPath))
            {
                Console.WriteLine("That path not exists.");
                Application.Exit();
            }*/

            listBox1.Items.Add("123.JPG");
        }
    

        private void AnswerTB_TextChanged(object sender, EventArgs e)
        {

        }

        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            TomlT["answer"].Add(counter.ToString(), AnswerTB.Text);
            SaveTOML(TomlT);

            Image image1 = Image.FromFile(ImagePath);
            image1.Save(FolderPath + "\\" + counter.ToString() + ".jpg", image1.RawFormat);
            counter += 1;

            MessageBox.Show("題目新增成功", counter.ToString()+"成功",
                                 MessageBoxButtons.YesNo,
                                 MessageBoxIcon.Question);
            UsertoolStripLabel.Text = "目前編號：" + counter.ToString();
            AnswerTB.Text = "";
            FileImportLable.Image = null;
            imageShow.Dispose();
        }

        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                FolderPath = folderBrowserDialog1.SelectedPath;
                Console.Write(FolderPath);
                PathtoolStripLabel.Text = FolderPath;
            }
            else
            {
                return;
            }

            // Determine whether the directory exists.
            if (!Directory.Exists(FolderPath))
            {
                Console.WriteLine("That path not exists.");
                return;
            }
        }

        private void toolStripLabel3_Click(object sender, EventArgs e)
        {
            saveFileDialog1.ShowDialog();

            if (saveFileDialog1.FileName != "")
            {
                string zipPath = saveFileDialog1.FileName;
                 ZipFile.CreateFromDirectory(FolderPath, zipPath);
            }
                
        }
    }
}
