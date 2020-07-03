using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tommy;

namespace PackageWizard
{
    public class toml
    {
        public void SaveTOML(String Data)
        {
            TomlTable toml = new TomlTable
            {
                ["title"] = "TOML Example",
                ["answer"] =
                {

                }
            };

            using (StreamWriter writer = new StreamWriter(File.OpenWrite("out.toml")))
                toml.ToTomlString(writer);
        }
    }
}
