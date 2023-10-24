import { SignUpCard } from "@/components/ui/card";
import { LinkButton } from "@/components/ui/linkButton";


const BlockSignUp = () => {
    return <section className="w-10/12 mx-auto h-screen flex items-center">
        <div className=" grid grid-cols-2   place-items-center  w-full">
            <SignUpCard>
                <span className="inline-block text-3xl font-medium">
                    Trouvez votre prochain <br /> mentor
                </span>

                <p className="py-8 text-lg">
                    Parcourez la liste de nos mentors pour vous <br /> aidez a avancer sur vos projet
                </p>
                <div className="flex gap-4">
                    <LinkButton href="#">
                        Inscription
                    </LinkButton>
                    <LinkButton href="#">
                        Poseez une question
                    </LinkButton>
                </div>
            </SignUpCard>
            <SignUpCard>
            <span className="inline-block text-3xl font-medium">
            Inspirez et guidez la <br/> prochaine génération
                </span>
             

                <p className="py-8 text-lg ">
                Rejoignez-nous en tant que mentor et faites une différence dès aujourd'hu
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