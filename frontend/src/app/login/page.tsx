"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import * as z from "zod"

import { Button } from "@/components/ui/button"
import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { toast } from "@/components/ui/use-toast"
import Image from "next/image"
import { LinkButtonOutline } from "@/components/ui/linkButton"

const FormSchema = z.object({
    email: z.string().min(2, {
        message: "Idenitfiant requise",
    }),
    password: z.string().min(2, {
        message: "Mot de passe requis",
    }),
})

export default function Login() {
    const form = useForm<z.infer<typeof FormSchema>>({
        resolver: zodResolver(FormSchema),
        defaultValues: {
            email: "",
            password: "",
        },
    })

    function onSubmit(data: z.infer<typeof FormSchema>) {

        toast({
            title: "You submitted the following values:",
            description: (
                <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
                    <code className="text-white">{JSON.stringify(data, null, 2)}</code>
                </pre>
            ),
        })
    }

    return (
        <section className="h-screen flex items-stretch justify-start ">
            <div className="grid grid-cols-4 only: w-full  ">
                <div className="w-full h-full bg-gray-200 flex items-center justify-content-center">
                    <div className="text-center">
                        <Image
                            src="/assets/logo/logo.png"
                            className=" mx-auto my-5  w-16 "
                            alt="xmentor-logo"
                            width={80}
                            height={80}
                        />
                        <p className="text-sm mx-auto p-4">
                            Une plateforme de mentorat  vous aide à vous améliorer en codage. Vous pouvez utiliser le même compte pour vous connecter à la fois à Codementor et à Arc.
                        </p>
                    </div>

                </div>
                <div className="w-full  col-span-3  items-center flex ">
                    <div className="w-[40%] ml-32">
                        <Form {...form}>
                            <form onSubmit={form.handleSubmit(onSubmit)} className="w-2/3 space-y-6">
                                <div className="text-2xl font-semibold">
                                    Se connecter a xmentor
                                </div>
                                <div className="flex gap-5 flex-col ">
                                    <LinkButtonOutline href={""} className="w-full  ">
                                        <div className="flex items-center gap-5  ">
                                            <Image
                                                src="/assets/icons/github.svg"
                                                className="w-8"
                                                alt="github"
                                                width={30}
                                                height={30}
                                            />
                                            <span className="">
                                                Se connecter avec Google
                                            </span>

                                        </div>
                                    </LinkButtonOutline>

                                    <LinkButtonOutline href={""} className="w-full  ">
                                        <div className="flex items-center gap-5  ">
                                            <Image
                                                src="/assets/icons/google.svg"
                                                className="w-7"
                                                alt="google"
                                                width={30}
                                                height={30}
                                            />
                                            <span>
                                                Se connecter avec Google
                                            </span>

                                        </div>
                                    </LinkButtonOutline>
                                    <div className="text-sm text-gray-600 text-center ">
                                        Ou se continuer par rmail
                                    </div>
                                </div>
                                <FormField
                                    control={form.control}
                                    name="email"
                                    render={({ field }) => (
                                        <FormItem className="flex gap-4 flex-col ">
                                            <FormLabel className="text-md ">Email</FormLabel>
                                            <FormControl>
                                                <Input className="h-12 px-4 ring-offset-xmentor/50 focus-visible:ring-xmentor/10 " type="email" placeholder="votre  mail" {...field} />
                                            </FormControl>
                                            <FormMessage />
                                        </FormItem>
                                    )}
                                />
                                <FormField control={form.control} name="password"
                                    render={({ field }) => (
                                        <FormItem>
                                            <FormLabel className="text-md">Mot de passe</FormLabel>
                                            <FormControl>
                                                <Input className="h-12 px-4 ring-offset-xmentor/50 focus-visible:ring-xmentor/10" type="password" placeholder="mot de passe " {...field} />
                                            </FormControl>
                                            <FormMessage />
                                        </FormItem>
                                    )} />
                                <div className="pt-5 ">
                                    <Button className="w-full bg-mentor hover:bg-xmentor/90 " type="submit">Connection</Button>
                                </div>
                            </form>
                        </Form>
                    </div>
                </div>
            </div>

        </section>

    )
}


