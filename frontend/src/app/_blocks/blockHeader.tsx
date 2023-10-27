import { LinkButton, LinkButtonOutline, LinkButtonSecondary } from "@/components/ui/linkButton";
import Slider from "@/components/ui/slider";
import React from "react";

 const BlockHeader: React.FC = () => {
    return <>
        <header className="w-full h-screen flex flex-col  justify-center ">
            <div className="w-10/12 mx-auto ">
                <div className="bg-gray-100 inline py-[.6rem] px-4 rounded-full">
                    <span className="inline-block mt-0 bg-clip-text text-transparent font-medium bg-gradient-to-r from-purple-600 to-pink-600 text-center ">
                        Apprenez, grandissez, excellez
                    </span>
                </div>
                <div className="py-8 w-3/6  ">

                    <h1 className="text-6xl  leading-tight font-semibold">
                        Élevez vos compétences  vers de nouveaux sommets
                    </h1>
                    <p className="w-5/6 py-4  text-xl  ">
                        La destination incontournable pour les développeurs en quête d'inspiration, d'apprentissage et de mentorat, créant un pont entre les générations de codeurs
                    </p>
                </div>
                <div className="inline-flex gap-8 ">
                    <LinkButtonSecondary  href="#"  >
                        <span>Trouver un mentor</span>
                    </LinkButtonSecondary>
                    <LinkButtonOutline href="#"  >
                        <span>Poser une question</span>
                    </LinkButtonOutline>
                </div>

            </div>
          <div className="overflow-hidden">
          <Slider />
          </div>
        </header>
    </>
}

export default BlockHeader