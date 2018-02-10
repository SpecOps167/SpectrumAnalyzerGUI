using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace controller
{
    class volume
    {
        public void volcontrol(String txt)
        {
            File.WriteAllText("volume.txt", txt);
        }
    }
}
