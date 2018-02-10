using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace controller
{
    public class control
    {
        public String visw = "40";
        public String vish = "20";
        public String idevice = "2";
        public String chunk = "4096";
        public String yshift = "300";
        public String bandc = "1.00185";
        public String logc = "1.35";
        public String powshift = "100";
        public String wscale = "900000";
        public String freqrange = "83";
        public String srate = "96000";
        public String dropfactor = "2";

        public void startcmd(String startopt, String visw, String vish, String idevice, String chunk, String yshift, String bandc, String logc, String powshift, String wscale, String freqrange, String srate, String dropfactor)
        {
            Process.Start("cmd", "/k python emulation23.py " + startopt + " " + visw + " " + vish + " " + idevice + " " + chunk + " " + yshift + " " + bandc + " " + logc + " " + powshift + " " + wscale + " " + freqrange + " " + srate + " " + dropfactor);
        }
    }
}
