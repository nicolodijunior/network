document.addEventListener('DOMContentLoaded', function(){
    //profile_info();
    //username = document.querySelector("#username_field").innerText;
    if(document.querySelector("#tof") != null){
        username = document.querySelector("#tof").dataset.f;
        document.querySelector("#tof").addEventListener('click', () => update_follow_stats(username));
    }

    document.querySelectorAll('#edit').forEach(function(button) {
        button.onclick = function(){
            post_id = button.dataset.postid;
            load_edit_field(post_id);
        }
    })

    document.querySelectorAll('.like_button').forEach(function(button) {
        button.onclick = function (){
            post_id = button.dataset.postid;
            like_post(post_id);
        }
    })
    //if()
    //document.querySelector("#tof").addEventListener('click', () => alert(username));
    //post_id = document.querySelector('#edit').dataset.postid;
    //document.querySelector('#edit').addEventListener('click', () => edit_post(post_id))
    //document.querySelector('#edit').addEventListener('click', () => alert(post_id))
})

function like_post(post_id){
    fetch(`/like/${post_id}`)
    .then(response => response.json())
    .then(data => {
        console.log(data.post_id); 
        console.log(data.liked);
        console.log(data.likes_qty); 
        return Promise.resolve();
    })
    .then(() => update_post(post_id))
    .catch(error => console.log('Error: ',error));
}

function update_post(post_id){
    fetch(`/update_post/${post_id}`)
    .then(response => response.json())
    .then(data => {
            console.log(data.liked);
            console.log(data.likes_qty);
            document.querySelector(`#likes_${post_id}`).textContent = "This post has "+data.likes_qty+" likes";
            if(!data.liked){
                if (document.querySelector(`#like_${post_id}`).classList.contains('dislike_btn')){
                    document.querySelector(`#like_${post_id}`).classList.remove("dislike_btn");
                }                
//                document.querySelector(`#like_${post_id}`).style.background = "#228be6";
            }
            else {
                document.querySelector(`#like_${post_id}`).classList.add("dislike_btn");
                //document.querySelector(`#like_${post_id}`).style.background = "#a5d8ff";
            }
        })
    .catch(error => console.log('Error: ',error));

}

function profile_info(username){
    fetch(`/profile_info/${username}`)
    .then(response => response.json())
    .then(data => {
        localStorage.clear();
        console.log("Followers: "+data.infos[1]);
        console.log("Following: "+data.infos[0]);
        document.querySelector("#followers").innerHTML = "Followers: "+data.infos[1];
        document.querySelector("#following").innerHTML = "Following: "+data.infos[0];
        follows = data.follows
        if (follows) {
            console.log("Follows True");
            document.querySelector("#tof").innerText = "Unfollow";
        }
        else {
            console.log("Follows False");
            document.querySelector("#tof").innerText = "Follow";
        }
        
        //else 
        //document.querySelector("#follows").innerHTML = data.
    });
}

// atualizar status de seguir e chamar profile_info para atualizar a página do usuário

function update_follow_stats(username){

    fetch(`/update_follow_stats/${username}`)
    .then(response => response.text())
    .then(text => {
        console.log(text);
        return Promise.resolve();
    })
    .then(() => {
        console.log("Complete");
        profile_info(username);
    });
}

function load_edit_field(post_id){
    document.querySelector(`#text_${post_id}`).style.display = 'none';
    const edit_post_div = document.createElement('div');
    const textarea = document.createElement('input');
    textarea.value = document.querySelector(`#text_${post_id}`).textContent;
    textarea.id = "edit_post_textarea";    
    textarea.classList.add("edit-loaded-field");
    //document.querySelector('#where_text_goes').append(textarea); 
    const button = document.createElement('button');
    button.id = "edit_post_button";
    button.innerHTML = "Save";
    button.type = "submit";  
    button.classList.add("post_btn");
    button.classList.add("save_btn");
    button.class = "";  
    button.onclick = function(){
        new_text = document.querySelector('#edit_post_textarea').value.trim();
        edit_post(post_id,new_text);
    };
    edit_post_div.append(textarea);
    edit_post_div.append(button);
    edit_post_div.id = "edit_post_div";
    document.querySelector(`#post_text_${post_id}`).append(edit_post_div);
}

function edit_post(post_id, text){
    fetch(`/edit_post/${post_id}/${text}`)
    .then(response => response.text())
    .then(text => console.log(text))
    .catch(error => console.log('Error: ',error));

    document.querySelector(`#post_text_${post_id}`).removeChild(edit_post_div);
    document.querySelector(`#text_${post_id}`).innerHTML = `<p>${text}</p>`;
    document.querySelector(`#text_${post_id}`).style.display = 'block';

    //document.querySelector('edit_post_textarea').style.display = 'none';
    //document.querySelector(`#text_${post_id}`).style.display = 'block';

    return false;
}





























/*
document.addEventListener('DOMContentLoaded', function() {
    //document.querySelector('.option-allposts').addEventListener('click', () => load_posts('allposts'));
    //load_posts('allposts')
    //document.querySelector('.user_link').forEach(btn => addEventListener('click', () => load_posts(username))) //addEventListener('click', () => load_posts(username));
})
*/
/*
function load_profile_stats(username){
    fetch(`/load_profile_stats/${username}`)
    .then(response => response.json())
    .then(data => {
        console.log(data);   
    });
}
*/
/*
function load_posts(wposts){
    
    fetch(`/posts/${wposts}`)
    .then(response => response.json())
    .then(data => {
        data.forEach(data => add_post(data, wposts));
    })
    .catch((error => {console.log('Error:', error);
}));
}
*/

/*
function add_post(post, wposts){
    console.log(post['text']);
    console.log(post.user);
    const em = document.createElement('div');
    em.innerHTML = `  
    <div class="all_posts">
            <div class="user_image">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu51XqkERN4KCU2HF526phPswwmMY9qjexFA&usqp=CAU" alt="profile image">
            </div>
            <div class="post_body">
                <div class="post_header">
                    <div class="post_header_text">
                        @usuario  ${post.user}               
                    </div>
                    <div class="post_text">
                        <p>${post.text}</p>
                    </div>
                    <div class="post_footer">
                        <span class="material-symbols-outlined">
                            add_reaction
                            </span>
                            <span class="material-symbols-outlined">
                                edit
                            </span>                            
                            <p>This post has ${post.likes} likes</p>
                    </div>
                </div>
            </div>
        </div>   
        `
        document.querySelector('#posts').append(em);
}
*/


/*
function new_post(){
    
    const text = document.querySelector('#post_text').value;

    fetch('/posts', {
        method:'POST',
        body: JSON.stringify({
            text: text
        })
    })
    .then(response => response.json())
    .then(result => console.log(result))
    .catch((error =>{
        console.log('Error', error);
    }));
    return false;
}
*/