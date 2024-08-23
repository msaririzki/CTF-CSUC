<?php

require("hm.php");
highlight_file(_FILE_);
if(isset($_GET['ikeh'])){
    $zee = $_GET['ikeh'];
    $ashel = 'budi_ari_atau_rektor_unram_ya';
    $get_flag = preg_replace("/$ashel/", '',$zee);
    if($get_flag === $ashel){
        echo "GG";
        echo $sus;
    }else {
        die("jawabannya ga bener!");
    }
}

?>