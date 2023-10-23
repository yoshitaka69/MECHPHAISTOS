<template>
    <div class="helloWorld">
        {{ msg2 }}
    </div>
</template>


<script>

export default{
    name: 'HelloWorld',
    props: {
        msg:String,
        msg2:String
    }
}

</script>
