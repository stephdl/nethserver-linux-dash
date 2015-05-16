<?php
namespace NethServer\Module\Dashboard\Applications;

/**
 * linux-dash web interface
 *
 * @author stephane de labrusse
 */
class LinuxDash extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Linux Dash";
    }

    public function getInfo()
    {
         $name = $this->getPlatform()->getDatabase('configuration')->getProp('linux-dash','Name');
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url' => "https://".$host[0]."/$name"
         );
    }
}


