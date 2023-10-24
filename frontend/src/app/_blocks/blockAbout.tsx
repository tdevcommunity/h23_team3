import { LinkButton, LinkButtonOutline } from "@/components/ui/linkButton";
import Image from "next/image";


export const BlockAbout: React.FC = () => {
    return <section className="py-10 w-10/12 mx-auto  ">
        <div>
            <div className="grid grid-cols-2  ">
                <h2 className="text-4xl font-medium py-6 text-slate-950  leading-relaxed">
                    Découvrez tout votre potentiel <br /> avec un mentor
                </h2>
                <div>
                    <p className="py-10  text-lg w-5/6 ">
                        Trouver le bon mentor peut faire la différence entre la stagnation et le succès dans votre parcours de développement. Avec un mentor expérimenté, vous pouvez bénéficier de conseils personnalisés, de précieuses connaissances et d'un réseau de soutien inestimable.
                    </p>
                    <LinkButton href="#" >
                        Obtenir de l'aide
                    </LinkButton>
                </div>
            </div>
        </div>
        <div>
            <div className="my-10 mt-20 text-center ">
                <h3 className="text-5xl font-medium py-6 text-slate-950  leading-relaxed">
                    Un océan de connaissances grace <br /> aux  mentors juste pour vous
                </h3>
                <p className="w-3/6  mx-auto py-5 text-lg ">
                    les mentors partagent régulièrement des articles informatifs, des guides pratiques et des astuces de premier plan pour vous aider à perfectionner vos compétences en développement. Explorez un trésor d'informations pour vous tenir à jour avec les dernières tendances
                </p>


            </div>


            <div className="grid grid-cols-2 place-items-center ">
                <div className="w-full">
                    <Image height={100} width={100} alt="" className="w-4/6 mx-auto  " src="/assets/illustrations/illustration1.svg" />
                </div>
                <div className="w-full">
                    <h4 className="text-4xl font-medium py-6  leading-relaxed">Trouvez des ressources <br /> ou fait vous suivre</h4>
                    <div className="py-5 flex gap-4 ">
                        <LinkButton href="#">
                            Ressources
                        </LinkButton>
                        <LinkButtonOutline href="#">
                            Poser une question
                        </LinkButtonOutline>
                    </div>
                </div>
            </div>

            <div className="grid grid-cols-2  place-items-center lace-content-center">
               
                <div className="w-fit mx-auto   ">
                    <h4 className="text-4xl font-medium py-6  leading-relaxed">Trouvez votre prochaine opportunité <br/> d'emploi</h4>
                    <div className="py-5 flex gap-4 ">
                        <LinkButton href="#">
                            Offre d'emploi
                        </LinkButton>
                        <LinkButtonOutline href="#">
                           S'inscrire
                        </LinkButtonOutline>
                    </div>
                </div>
                 <div className="w-full ">
                    <Image height={100} width={100} alt="" className="w-4/6  -scale-x-1 " src="/assets/illustrations/illustration2.svg" />
                </div>
            </div>
        </div>
    </section>
}

export default BlockAbout;