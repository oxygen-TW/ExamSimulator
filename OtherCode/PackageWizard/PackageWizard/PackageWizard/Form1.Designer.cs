namespace PackageWizard
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.FileImportLable = new System.Windows.Forms.Label();
            this.AnswerTB = new System.Windows.Forms.TextBox();
            this.WriteBtn = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.toolStripLabel1 = new System.Windows.Forms.ToolStripLabel();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripLabel2 = new System.Windows.Forms.ToolStripLabel();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.PathtoolStripLabel = new System.Windows.Forms.ToolStripLabel();
            this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
            this.UsertoolStripLabel = new System.Windows.Forms.ToolStripLabel();
            this.toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripLabel3 = new System.Windows.Forms.ToolStripLabel();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.toolStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // FileImportLable
            // 
            this.FileImportLable.AllowDrop = true;
            this.FileImportLable.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.FileImportLable.Font = new System.Drawing.Font("微軟正黑體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.FileImportLable.Location = new System.Drawing.Point(33, 82);
            this.FileImportLable.Name = "FileImportLable";
            this.FileImportLable.Size = new System.Drawing.Size(800, 600);
            this.FileImportLable.TabIndex = 0;
            this.FileImportLable.Text = "將圖片拖拉至此";
            this.FileImportLable.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.FileImportLable.DragDrop += new System.Windows.Forms.DragEventHandler(this.FileImportLable_DragDrop);
            this.FileImportLable.DragEnter += new System.Windows.Forms.DragEventHandler(this.FileImportLable_DragEnter);
            // 
            // AnswerTB
            // 
            this.AnswerTB.Location = new System.Drawing.Point(36, 45);
            this.AnswerTB.Name = "AnswerTB";
            this.AnswerTB.Size = new System.Drawing.Size(797, 25);
            this.AnswerTB.TabIndex = 1;
            this.AnswerTB.TextChanged += new System.EventHandler(this.AnswerTB_TextChanged);
            // 
            // WriteBtn
            // 
            this.WriteBtn.Location = new System.Drawing.Point(957, 2);
            this.WriteBtn.Name = "WriteBtn";
            this.WriteBtn.Size = new System.Drawing.Size(75, 23);
            this.WriteBtn.TabIndex = 2;
            this.WriteBtn.Text = "button1";
            this.WriteBtn.UseVisualStyleBackColor = true;
            this.WriteBtn.Click += new System.EventHandler(this.WriteBtn_Click);
            // 
            // folderBrowserDialog1
            // 
            this.folderBrowserDialog1.SelectedPath = ".";
            // 
            // toolStrip1
            // 
            this.toolStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripLabel1,
            this.toolStripSeparator1,
            this.toolStripLabel2,
            this.toolStripSeparator2,
            this.PathtoolStripLabel,
            this.toolStripSeparator3,
            this.UsertoolStripLabel,
            this.toolStripSeparator4,
            this.toolStripLabel3});
            this.toolStrip1.Location = new System.Drawing.Point(0, 0);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(872, 25);
            this.toolStrip1.TabIndex = 3;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // toolStripLabel1
            // 
            this.toolStripLabel1.Name = "toolStripLabel1";
            this.toolStripLabel1.Size = new System.Drawing.Size(84, 22);
            this.toolStripLabel1.Text = "選擇資料夾";
            this.toolStripLabel1.Click += new System.EventHandler(this.toolStripLabel1_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(6, 25);
            // 
            // toolStripLabel2
            // 
            this.toolStripLabel2.Name = "toolStripLabel2";
            this.toolStripLabel2.Size = new System.Drawing.Size(54, 22);
            this.toolStripLabel2.Text = "下一題";
            this.toolStripLabel2.Click += new System.EventHandler(this.toolStripLabel2_Click);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(6, 25);
            // 
            // PathtoolStripLabel
            // 
            this.PathtoolStripLabel.Name = "PathtoolStripLabel";
            this.PathtoolStripLabel.Size = new System.Drawing.Size(84, 22);
            this.PathtoolStripLabel.Text = "目前資料夾";
            // 
            // toolStripSeparator3
            // 
            this.toolStripSeparator3.Name = "toolStripSeparator3";
            this.toolStripSeparator3.Size = new System.Drawing.Size(6, 25);
            // 
            // UsertoolStripLabel
            // 
            this.UsertoolStripLabel.Name = "UsertoolStripLabel";
            this.UsertoolStripLabel.Size = new System.Drawing.Size(69, 22);
            this.UsertoolStripLabel.Text = "指示標籤";
            // 
            // toolStripSeparator4
            // 
            this.toolStripSeparator4.Name = "toolStripSeparator4";
            this.toolStripSeparator4.Size = new System.Drawing.Size(6, 25);
            // 
            // toolStripLabel3
            // 
            this.toolStripLabel3.Name = "toolStripLabel3";
            this.toolStripLabel3.Size = new System.Drawing.Size(84, 22);
            this.toolStripLabel3.Text = "建立壓縮檔";
            this.toolStripLabel3.Click += new System.EventHandler(this.toolStripLabel3_Click);
            // 
            // saveFileDialog1
            // 
            this.saveFileDialog1.DefaultExt = "zip";
            this.saveFileDialog1.Filter = "|Zip file|*.zip|";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(872, 753);
            this.Controls.Add(this.toolStrip1);
            this.Controls.Add(this.WriteBtn);
            this.Controls.Add(this.AnswerTB);
            this.Controls.Add(this.FileImportLable);
            this.Name = "Form1";
            this.Text = "跑台測驗程式題目產生器";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label FileImportLable;
        private System.Windows.Forms.TextBox AnswerTB;
        private System.Windows.Forms.Button WriteBtn;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripLabel toolStripLabel1;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripLabel toolStripLabel2;
        private System.Windows.Forms.ToolStripLabel PathtoolStripLabel;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
        private System.Windows.Forms.ToolStripLabel UsertoolStripLabel;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator4;
        private System.Windows.Forms.ToolStripLabel toolStripLabel3;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
    }
}

