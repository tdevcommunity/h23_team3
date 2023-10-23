import RoundButton from "../roundButton";

const FirstSection = () => {
    return (
        <div className="text-center">
            <RoundButton
                bgColorClass="bg-gray-200"
                content={
                    <p className="text-[12px] mt-0 bg-clip-text text-transparent bg-gradient-to-r from-purple-600 to-pink-600 text-center font-bold">
                        Apprenez, Agrandissez, Excellez
                    </p>
                }
            />
            <h1 className="mt-4 text-[45px] font-semibold w-[60vw] mx-auto">
                Élevez vos compétences en développement vers de nouveaux sommets.
            </h1>
            <p className="mt-2 mx-auto max-w-xl ">
                La destination incontournable pour les développeurs en quête
                d'inspiration, d'apprentissage et de mentorat, créant un pont entre les
                générations de codeurs.
            </p>
            <div className="mt-8 flex justify-center">
                <RoundButton bgColorClass="bg-purple-600" content={
                    <p className="mt-2 text-base text-white">
                        Trouver un mentor
                    </p>
                } />
                <div className="mx-2"></div>
                <RoundButton bgColorClass="transparent" border="bg-gray-500" content={
                    <p className="mt-2 text-base text-black">Poser une question</p>
                } />
            </div>

        </div>
    );
};

export default FirstSection;
