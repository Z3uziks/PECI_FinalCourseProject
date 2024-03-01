import React, { useState } from 'react';
import ReactPlayer from 'react-player';

function VideoPlayer() {
    // Estado para controlar se a descrição está expandida ou não
    const [isExpanded, setIsExpanded] = useState(false);

    // Texto de exemplo da descrição
    const description = "Esta é a descrição do vídeo. Aqui pode ir um texto mais longo que explique o conteúdo do vídeo, detalhes sobre a produção, créditos, ou qualquer outra informação relevante que você queira incluir.";

    // Função para alternar a visibilidade
    const toggleDescription = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div>
            <ReactPlayer
                url="demo.mp4"
                width="100%"
                height="100%"
                controls
            />
            <p><br></br></p>
            <div className=" w-11/12 mx-auto">
                <h2><b><u>Video Description</u></b></h2>
                {/* Renderiza a descrição com base no estado isExpanded */}
                <p>
                    {isExpanded ? description : `${description.substring(0, 100)}...`}
                </p>
                {/* Botão para expandir/retrair a descrição */}
                <button onClick={toggleDescription}>
                    {isExpanded ? 'Show Less' : 'Show More'}
                </button>
            </div>
        </div>
    );
}

export default VideoPlayer;
