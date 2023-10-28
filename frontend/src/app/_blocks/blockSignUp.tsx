import { SignUpCard } from "@/components/ui/card";
import { LinkButton ,LinkButtonOutline } from "@/components/ui/linkButton";


const BlockSignUp = () => {
    return <section className="w-10/12 mx-auto py-36 flex items-center">
        <div className=" grid grid-cols-2   place-items-center  w-full">
            <SignUpCard>
                <span className="bg-green-300 text-sm  text-black py-2 px-3 mb-2 rounded-full inline-block ">
                Vous avez besoin d’assitance ?
                </span>
                <span className="inline-block text-3xl font-medium">
                    Trouvez votre prochain <br /> mentor
                </span>

                <p className="py-8 text-lg">
                    Parcourez la liste de nos mentors pour vous <br /> aidez a avancer sur vos projets
                </p>
                <div className="flex gap-4">
                    <LinkButton href="#">
                        Inscription
                    </LinkButton>
                    <LinkButtonOutline href="#">
                        Posez une question
                    </LinkButtonOutline>
                </div>
            </SignUpCard>
            <SignUpCard>
            <span className="bg-purple-300 text-sm  text-black py-2 px-3 mb-2 rounded-full inline-block ">
            Vous etes expert
                </span>
            <span className="inline-block text-3xl font-medium">
            Inspirez et guidez la <br/> prochaine génération
                </span>
             

                <p className="py-8 text-lg ">
                Rejoignez-nous en tant que mentor et faites une différence dès aujourd'hui
                </p>
                <div>
                    <LinkButton href="#">
                        creer mon profile
                    </LinkButton>

                </div>
            </SignUpCard>

        </div>
    </section>
}
export default BlockSignUp;