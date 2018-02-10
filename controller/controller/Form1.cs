using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace controller
{
    public partial class Form1 : Form
    {
        control c = new controller.control();

        public Form1()
        {
            InitializeComponent();
            start.Click += startbtn;
            ledbtn.Click += startled;
            volume.Click += volumebtn;

            visw.Text = c.visw;
            vish.Text = c.vish;
            idevice.Text = c.idevice;
            chunk.Text = c.chunk;
            yshift.Text = c.yshift;
            bandc.Text = c.bandc;
            logc.Text = c.logc;
            powshift.Text = c.powshift;
            wscale.Text = c.wscale;
            freqrange.Text = c.freqrange;
            srate.Text = c.srate;
            dropfactor.Text = c.dropfactor;
        }
        public void startbtn(object sender, System.EventArgs e)
        {
            c.startcmd("emulated", visw.Text, vish.Text, idevice.Text, chunk.Text, yshift.Text, bandc.Text, logc.Text, powshift.Text, wscale.Text, freqrange.Text, srate.Text, dropfactor.Text);
        }
        public void startled(object sender, System.EventArgs e)
        {
            c.startcmd("double", visw.Text, vish.Text, idevice.Text, chunk.Text, yshift.Text, bandc.Text, logc.Text, powshift.Text, wscale.Text, freqrange.Text, srate.Text, dropfactor.Text);
        }
        public void volumebtn(object sender, System.EventArgs e)
        {
            volume v = new controller.volume();
            int vol = volumebar.Value;
            v.volcontrol(vol.ToString());
        }
    }
}
